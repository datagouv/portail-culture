# Réutilisation phare
ID : section_reutilisation

## Objectif
Mettre en valeur les jeux de données les plus consultés sur la plateforme, afin d’encourager l’exploration des ressources jugées pertinentes ou utiles par la communauté. Ce bloc permet de valoriser les données à fort impact et de guider les utilisateurs vers les contenus les plus visités.

## Automatisation
Section éditoriale non automatisée

## Périodicité d’actualisation
Mensuelle

## Contenu
  - Colonne droite
    - titre section : non
    - titre : Journées Européennes du patrimoine 
    - sous-titre : Réutilisation phare du mois
    - paragraphe : "Cartes.gouv / IGN
      A l’occasion des journées européennes du patrimoine, découvrez les lieux avec cartes.gouv.fr"
    - Réalisé à partir des données ouvertes (lien vers jeu de données)
    - Bouton : "Découvrez l’application IGN - Cartes" lien vers application

Colonne gauche
  - image (hébergement au sein du repertoire assets) : pour test : https://github.com/datagouv/portail-culture/blob/Documentation/Doc_CustomComponents/Doc_CustomAssets/GeoDataPatrimoine.png

## Composant DSFR
https://www.systeme-de-design.gouv.fr/version-courante/fr/composants/zone-d-expression-visuelle/design-de-la-zone-d-expression-visuelle 
https://www.systeme-de-design.gouv.fr/v1.14/asset/component/composition/design/variation/do-7.png

## Exemple
![Card_image](https://github.com/datagouv/portail-culture/blob/Documentation/Doc_CustomComponents/Doc_CustomAssets/Exemple_reutilisation_phare.png?raw=true)

## Code

```
   - title: ''
        content: >-
          <section class="fr-container fr-my-5w" id="section_reutilisation">
            <div class="fr-grid-row fr-grid-row--gutters fr-grid-row--middle">
              <div class="fr-col-12 fr-col-md-6">
                <img src="[/culture/assets/GeoDataPatrimoine.png](https://github.com/datagouv/portail-culture/blob/Documentation/Doc_CustomComponents/Doc_CustomAssets/Exemple_reutilisation_phare.png?raw=true)" alt="Réutilisation : Cartes IGN pour les JEP" class="fr-responsive-img" />
              </div>
              <div class="fr-col-12 fr-col-md-6">
                <h3 class="fr-h5 fr-mb-2w">Réutilisation phare du mois</h3>
                <h4 class="fr-h6 fr-mb-2w">Journées Européennes du Patrimoine</h4>
                <p class="fr-text--sm fr-mb-2w">
                  <strong>Cartes.gouv / IGN</strong><br>
                  À l’occasion des Journées Européennes du Patrimoine, découvrez les lieux avec <a href="https://cartes.gouv.fr" target="_blank">cartes.gouv.fr</a>.
                </p>
                <p class="fr-text--sm fr-mb-3w">
                  Réalisé à partir des <a href="https://www.data.gouv.fr/fr/datasets/journees-europeennes-du-patrimoine-2024" target="_blank">données ouvertes du ministère</a>.
                </p>
                <a href="https://cartes.gouv.fr" class="fr-btn" target="_blank" rel="noopener">
                  Découvrez l’application IGN - Cartes
                </a>
              </div>
            </div>
```
