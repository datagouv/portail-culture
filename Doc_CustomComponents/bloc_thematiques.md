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
    <div class="fr-tags-group" style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
      <a href="/datasets?tags=archives" class="fr-tag" aria-label="Dossier d’archives">🗃️ Archives</a>
      <a href="/datasets?tags=architecture" class="fr-tag" aria-label="Architecture et construction">🏗️ Architecture</a>
      <a href="/datasets?tags=arts-plastiques" class="fr-tag" aria-label="Arts plastiques">🎨 Arts plastiques</a>
      <a href="/datasets?tags=cinema" class="fr-tag" aria-label="Cinéma">🎬 Cinéma</a>
      <a href="/datasets?tags=spectacle-vivant" class="fr-tag" aria-label="Spectacle vivant">🎭 Spectacle vivant</a>
      <a href="/datasets?tags=livre" class="fr-tag" aria-label="Livre et lecture">📚 Livre & lecture</a>
      <a href="/datasets?tags=musique" class="fr-tag" aria-label="Musique">🎵 Musique</a>
      <a href="/datasets?tags=presse" class="fr-tag" aria-label="Presse écrite">📰 Presse écrite</a>
      <a href="/datasets?tags=musees" class="fr-tag" aria-label="Musées">🖼️ Musées</a>
      <a href="/datasets?tags=langue" class="fr-tag" aria-label="Langue et communication">💬 Langue</a>
      <a href="/datasets?tags=industries-culturelles" class="fr-tag" aria-label="Industries culturelles et créatives">💡 Industries culturelles</a>
    </div>
```

