# Jeux de données par Thématiques

via YAML et html

Exemple d'un ajout d'une section html directement au sein du Yaml :
![Card_image](https://github.com/datagouv/portail-culture/blob/Documentation/Doc_CustomComponents/Doc_CostomAssets/CardsProfils.png)

```
- title: Explorer par thématique
        id: bloc_thematiques
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

