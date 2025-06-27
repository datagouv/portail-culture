# Documentation : Intégration d'un bloc dynamique via JSON dans la page d'accueil

## Objectif
Afficher un bloc de cartes dynamiques sur la page d’accueil, alimenté depuis un fichier JSON externe, contrôlé via le fichier `home.yaml`, et affiché via un composant Vue.

---

## Structure des fichiers

### 1. `public/culture/cards.json`
Contient la liste des cartes à afficher :

```json
[
  {
    "title": "Découvrir les bibliothèques",
    "url": "/datasets/bibliothèques",
    "description": "Panorama des ressources numériques proposées par les bibliothèques.",
    "image": {
      "src": "/img/bib.jpg",
      "alt": "Bibliothèque numérique"
    }
  },
  ...
]
```

### 2. `home.yaml`
Activer et configurer le bloc dynamique :

```yaml
- title: Explorer les données culturelles
  cards_section:
    enabled: true
    heading: "Explorer les données culturelles"
    source: "culture/cards.json"
```

### 3. `src/components/CardsSectionComponent.vue`
Composant Vue compatible DSFR qui charge et affiche les cartes :

```vue
<template>
  <section class="fr-container fr-py-6w">
    <h2 class="fr-h3">{{ heading }}</h2>
    <div class="fr-grid-row fr-grid-row--gutters">
      <div
        v-for="(card, i) in cards"
        :key="i"
        class="fr-col-12 fr-col-md-6 fr-col-lg-4"
      >
        <div class="fr-card fr-enlarge-link">
          <div class="fr-card__body">
            <div class="fr-card__content">
              <h3 class="fr-card__title">
                <a :href="card.url">{{ card.title }}</a>
              </h3>
              <p class="fr-card__desc">{{ card.description }}</p>
            </div>
          </div>
          <div class="fr-card__header" v-if="card.image">
            <div class="fr-card__img">
              <img
                class="fr-responsive-img"
                :src="card.image.src"
                :alt="card.image.alt || ''"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted, defineProps } from 'vue'

const props = defineProps<{
  heading: string
  source: string
}>()

const cards = ref([])

onMounted(async () => {
  try {
    const res = await fetch('/' + props.source)
    cards.value = await res.json()
  } catch (e) {
    console.error('Erreur lors du chargement des cartes JSON', e)
  }
})
</script>
```

### 4. `src/views/HomeView.vue`

#### a. Importer le composant :
```ts
import CardsSectionComponent from '@/components/CardsSectionComponent.vue'
```

#### b. L'afficher dans la boucle des sections :
```vue
<CardsSectionComponent
  v-if="item.cards_section?.enabled"
  :heading="item.cards_section.heading"
  :source="item.cards_section.source"
/>
```

---

## Rendu attendu
Un bloc de type carte DSFR affichant dynamiquement les données du fichier JSON. Les éditeurs de contenu peuvent activer ou désactiver ce bloc via YAML, sans intervention d’un développeur.

---

## Bonnes pratiques
- Le fichier JSON est placé dans `public/` pour un accès direct via URL.
- Le composant est réutilisable : changer le `source` permet de charger un autre fichier.
- Le code respecte les classes du Design System de l’État (DSFR).

---
