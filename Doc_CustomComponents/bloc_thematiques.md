# Jeux de données par Thématiques

via YAML + composant custom vue
```
- id: bloc_thematiques
  sub_section_tags:
    title: Explorer par thématique
    tags:
      - label: "🗃️ Archives"
        url: "/datasets?tags=archives"
        aria_label: "Dossier d’archives"
      - label: "🏗️ Architecture"
        url: "/datasets?tags=architecture"
        aria_label: "Architecture et construction"
      - label: "🎨 Arts plastiques"
        url: "/datasets?tags=arts-plastiques"
        aria_label: "Arts plastiques"
      - label: "🎬 Cinéma"
        url: "/datasets?tags=cinema"
        aria_label: "Cinéma"
      - label: "🎭 Spectacle vivant"
        url: "/datasets?tags=spectacle"
        aria_label: "Spectacle vivant"
      - label: "📚 Livre & lecture"
        url: "/datasets?tags=livre"
        aria_label: "Livre et lecture"
      - label: "🎵 Musique"
        url: "/datasets?tags=musique"
        aria_label: "Musique"
      - label: "📰 Presse écrite"
        url: "/datasets?tags=presse"
        aria_label: "Presse écrite"
      - label: "🖼️ Musées"
        url: "/datasets?tags=musee"
        aria_label: "Musées"
      - label: "💬 Langue"
        url: "/datasets?tags=langue"
        aria_label: "Langue et communication"
      - label: "💡 Industries culturelles"
        url: "/datasets?tags=industries-culturelles"
        aria_label: "Industries culturelles et créatives"

```
## via HTML 

```
- id: bloc_thematiques
  title: Explorer par thématique
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

