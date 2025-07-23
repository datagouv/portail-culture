# Jeux de données par Thématiques
Id : section_thematiques

## Objectif
Offrir un point d’entrée visuel, intuitif et thématique à la diversité des données culturelles. Favorise l’exploration ciblée selon les centres d’intérêt des utilisateurs.

## Automatisation
Paramétrage manuel de l’encart

## Périodicité d’actualisation
Vérification annuelle de la liste des thématiques

## Composant DSFR
DsfrTags (type "Tag lien") Style : fr-tag, fr-tag--sm, fr-tag—clickable

## Fonctionnement
Chaque tag est cliquable (redirige vers /explore/?refine.theme=...) contient un emoji illustratif + libellé clair reprend les thématiques du site data.culture.gouv.fr

## Exemple d'un ajout d'une section html directement au sein du Yaml :
![Card_image](https://github.com/datagouv/portail-culture/blob/Documentation/Doc_CustomComponents/Doc_CustomAssets/bloc_thematiques.png)

# Tableau des thématiques

| Thématique             | Emoji   | Unicode   | Libellé accessibilité (ARIA)        | Description                                          |
|:-----------------------|:--------|:----------|:------------------------------------|:-----------------------------------------------------|
| Archives               | 🗃️      | U+1F5C3   | Archives                            | Meuble d’archives, évocateur de conservation         |
| Architecture           | 🏗️      | U+1F3D7   | Architecture                        | Grue de chantier, symbolise la construction          |
| Arts plastiques        | 🎨      | U+1F3A8   | Arts plastiques                     | Palette de peinture, monde artistique et visuel      |
| Cinéma                 | 🎬      | U+1F3AC   | Cinéma                              | Clap de tournage, identifie immédiatement le cinéma  |
| Spectacle vivant       | 🎭      | U+1F3AD   | Spectacle vivant                    | Masques de théâtre, symboles universels du spectacle |
| Livre & lecture        | 📚      | U+1F4DA   | Livre et lecture                    | Livres empilés, lecture et éducation                 |
| Musique                | 🎵      | U+1F3B5   | Musique                             | Note musicale, facilement identifiable               |
| Presse écrite          | 📰      | U+1F4F0   | Presse écrite                       | Journal imprimé, média traditionnel                  |
| Musées                 | 🖼️      | U+1F5BC   | Musées                              | Tableau encadré, musée ou galerie d’art              |
| Langue                 | 💬      | U+1F4AC   | Langue                              | Bulle de dialogue, évoque la parole et la langue     |
| Industries culturelles | 💡      | U+1F4A1   | Industries culturelles et créatives | Ampoule, image d’idées, d’innovation créative        |


## Code Yaml + html
```
- title: 🧭 Choisissez votre domaine culturel

        id: section_thematiques
        content: |
          <ul class="fr-tags-group">
            <li><a class="fr-tag" href="/datasets?tags=archives" aria-label="Dossier d’archives">🗃️ Archives</a></li>
            <li><a class="fr-tag" href="/datasets?tags=architecture" aria-label="Architecture et construction">🏗️ Architecture</a></li>
            <li><a class="fr-tag" href="/datasets?tags=arts-plastiques" aria-label="Arts plastiques">🎨 Arts plastiques</a></li>
            <li><a class="fr-tag" href="/datasets?tags=cinema" aria-label="Cinéma">🎬 Cinéma</a></li>
            <li><a class="fr-tag" href="/datasets?tags=spectacle-vivant" aria-label="Spectacle vivant">🎭 Spectacle vivant</a></li>
            <li><a class="fr-tag" href="/datasets?tags=livre" aria-label="Livre et lecture">📚 Livre & lecture</a></li>
            <li><a class="fr-tag" href="/datasets?tags=musique" aria-label="Musique">🎵 Musique</a></li>
            <li><a class="fr-tag" href="/datasets?tags=presse" aria-label="Presse écrite">📰 Presse écrite</a></li>
            <li><a class="fr-tag" href="/datasets?tags=musees" aria-label="Musées">🖼️ Musées</a></li>
            <li><a class="fr-tag" href="/datasets?tags=langue" aria-label="Langue et communication">💬 Langue</a></li>
            <li><a class="fr-tag" href="/datasets?tags=industries-culturelles" aria-label="Industries culturelles et créatives">💡 Industries culturelles</a></li>
          </ul>

```

