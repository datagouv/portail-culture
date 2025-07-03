
# Documentation : Intégration de la section "Mission" via JSON et composant personnalisé

## Objectif

Afficher une section full width "Mission" sur la page d’accueil, activable depuis `home.yaml`, avec des données extraites d’un fichier JSON, et un composant personnalisé stocké dans `custom/culture/components`.

---

## Structure des fichiers

### 1. `public/culture/data/mission.json`

```json
{
  "title": "La mission de culture.data.gouv.fr",
  "subtitle": "Simplifier l’accès aux données culturelles publiques",
  "text": "L’ouverture des données culturelles renforce la transparence, permet de nouveaux usages, et valorise les institutions publiques.",
  "objectives": [
    {
      "title": "Faciliter la découvrabilité",
      "icon": "search-line"
    },
    {
      "title": "Améliorer la qualité",
      "icon": "mail-line"
    },
    {
      "title": "Encourager la réutilisation",
      "icon": "check-line"
    }
  ],
  "link": {
    "label": "En savoir plus",
    "url": "/about"
  }
}
```

### 2. `custom/culture/components/MissionSectionComponent.vue`

```vue
<template>
  <section class="fr-py-6w fr-container-fluid text-white" style="background-color: #242424;">
    <div class="fr-container">
      <div class="fr-mb-6w">
        <h2 class="fr-h4">{{ data.title }}</h2>
        <h3 class="fr-h2">{{ data.subtitle }}</h3>
        <p class="fr-text--lead">{{ data.text }}</p>
      </div>
      <div class="fr-grid-row fr-grid-row--gutters fr-mt-6w">
        <div
          v-for="(goal, i) in data.objectives"
          :key="i"
          class="fr-col-12 fr-col-md-4"
        >
          <div class="fr-card fr-card--no-border fr-p-4w h-full" style="background-color: #242424; color: white;">
            <div class="fr-icon fr-mb-2w">
              <i :class="'ri-' + goal.icon"></i>
            </div>
            <p class="fr-h6" style="color: white;">{{ goal.title }}</p>
          </div>
        </div>
      </div>
      <div v-if="data.link" class="fr-mt-6w text-center">
        <a :href="data.link.url" class="fr-btn">{{ data.link.label }}</a>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted, defineProps } from 'vue'

const props = defineProps<{ source: string }>()

const data = ref({
  title: '',
  subtitle: '',
  text: '',
  objectives: [],
  link: null
})

onMounted(async () => {
  const res = await fetch('/' + props.source)
  data.value = await res.json()
})
</script>
```

### 3. `home.yaml`

Ajoute dans `website.homepage.sections` :

```yaml
- title: Mission
  mission_section:
    enabled: true
    source: culture/data/mission.json
```

### 4. `src/views/HomeView.vue`

Importer le composant :

```ts
import MissionSectionComponent from '@/custom/culture/components/MissionSectionComponent.vue'
```

L’utiliser dans la boucle des sections, **en dehors** du bloc `.fr-container` :

```vue
<div v-for="item in sectionsHomePage" :key="item">
  <div class="fr-container hero-text">
    <h4 v-if="item.title">{{ item.title }}</h4>
    <span v-html="fromMarkdown(item.content)" />
    <div class="fr-mt-4w fr-col-md-12 datagouv-components">
      <SubSectionDatasets v-if="item.sub_section_datasets" :subsection="item.sub_section_datasets" />
      <SubSectionCards v-if="item.sub_section_cards" :subsection="item.sub_section_cards" />
      <SubSectionTiles v-if="item.sub_section_tiles" :subsection="item.sub_section_tiles" />
      <SubSectionButtons v-if="item.sub_section_buttons" :subsection="item.sub_section_buttons" />
    </div>
  </div>
  <MissionSectionComponent v-if="item.mission_section?.enabled" :source="item.mission_section.source" />
</div>
```

---

## Rendu attendu

Une section visuellement intégrée au style DSFR, en **full-width** (#242424), avec un titre, sous-titre, description et 3 cartes d’objectifs.

## Bonnes pratiques
- Utiliser `custom/culture/components/` pour les blocs spécifiques à la transversale
- Utiliser `public/culture/data/` pour les données JSON

---


