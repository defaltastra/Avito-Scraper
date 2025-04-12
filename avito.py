import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

def scraper_avito_vehicules(pages=1):
    tous_vehicules = []
    url_base = "https://www.avito.ma/fr/maroc/v%C3%A9hicules"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://www.avito.ma/'
    }
    
    for page in range(1, pages + 1):
        if page == 1:
            url = url_base
        else:
            url = f"{url_base}?o={page}"
            
        print(f"Récupération page {page}/{pages}: {url}")
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            annonces = soup.select('a.sc-1jge648-0')
            
            for annonce in annonces:
                try:
                    donnees_vehicule = {}
                    
                    titre_elem = annonce.select_one('p.sc-1x0vz2r-0.iHApav')
                    donnees_vehicule['voiture'] = titre_elem.text.strip() if titre_elem else 'N/A'
                    
                    prix_elem = annonce.select_one('p.sc-1x0vz2r-0.dJAfqm')
                    donnees_vehicule['prix'] = prix_elem.text.strip() if prix_elem else 'Prix non spécifié'
                    
                    ville_elem = annonce.select_one('p.sc-1x0vz2r-0.layWaX[style*="line-height:1"]')
                    if ville_elem:
                        ville_text = ville_elem.text.strip()
                        if 'dans ' in ville_text:
                            ville_partie = ville_text.split('dans ')[1]
                            if ',' in ville_partie:
                                donnees_vehicule['ville'] = ville_partie.split(',')[0].strip()
                            else:
                                donnees_vehicule['ville'] = ville_partie.strip()
                        else:
                            donnees_vehicule['ville'] = 'N/A'
                    else:
                        donnees_vehicule['ville'] = 'N/A'
                    
                    modele_texte = donnees_vehicule['voiture'].split()
                    if len(modele_texte) >= 2:
                        donnees_vehicule['modele'] = modele_texte[0] + ' ' + modele_texte[1]
                    else:
                        donnees_vehicule['modele'] = 'Non spécifié'
                    
                    tous_vehicules.append(donnees_vehicule)
                    
                except Exception as e:
                    print(f"Erreur: {e}")
                    continue
            
            time.sleep(random.uniform(1, 3))
            
        except Exception as e:
            print(f"Erreur page {page}: {e}")
            continue
    
    df = pd.DataFrame(tous_vehicules)
    return df

def sauvegarder_excel(df, nom_fichier="vehicules_avito.xlsx"):
    df.to_excel(nom_fichier, index=False)
    print(f"Données sauvegardées dans {nom_fichier}")

def main():
    pages_a_scraper = 1 # a modifier si vous voulez plus de page
    
    print(f"Démarrage de la récupération des annonces de véhicules sur Avito Maroc...")
    df = scraper_avito_vehicules(pages=pages_a_scraper)
    
    print(f"\nRécupération terminée. Total d'annonces trouvées: {len(df)}")
    
    try:
        sauvegarder_excel(df)
    except Exception as e:
        print(f"Impossible de sauvegarder en Excel: {e}")
    
    print("\nTerminé!")

if __name__ == "__main__":
    main()