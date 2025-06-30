
# Documentation : Intégration de la section "Réutilisations et Communauté"

## Objectif

Créer et intégrer un composant valorisant les réutilisations et la communauté data.gouv.fr.

---

## Fichiers

### 1. JSON à placer dans `public/culture/data/reuses.json`

```json
{
  "title": "Une communauté dynamique et engagée",
  "description": "Partagez votre usage des données et échangez entre producteurs et réutilisateurs de données.",
  "stats": [
    { "label": "Réutilisations", "value": "4K" },
    { "label": "Utilisateurs", "value": "122K" },
    { "label": "Discussions", "value": "15K" }
  ],
  "partners": [
    { "alt": "Le Monde", "src": "/nuxt_images/organizations/lemonde.png" },
    { "alt": "Google Maps", "src": "/nuxt_images/organizations/googlemaps.png" },
    { "alt": "Libération", "src": "/nuxt_images/organizations/liberation.png" },
    { "alt": "Fondation Wikimedia", "src": "/nuxt_images/organizations/wikimedia.png" }
  ],
  "link": {
    "label": "Voir les réutilisations",
    "url": "/fr/reuses/"
  },
  "cta": {
    "label": "Comment réutiliser des données ?",
    "url": "/fr/pages/onboarding/reutilisateurs/"
  }
}
```

---

### 2. Composant Vue `custom/culture/components/ReuseCommunitySection.vue`

```vue
<template>
  <section class="fr-container-fluid bg-[#f6f6f6]">
    <div class="px-6 flex justify-center py-8 sm:py-24">
      <div class="w-full max-w-lg space-y-8">
        <div class="space-y-2">
          <img
            class="h-16 grayscale"
            src="/_ipx/_/illustrations/discussion.svg"
            alt=""
          />
          <h2 class="text-3xl text-gray-title font-extrabold">
            {{ data.title }}
          </h2>
          <p>{{ data.description }}</p>
        </div>
        <div class="flex flex-col sm:flex-row sm:justify-between gap-4">
          <div v-for="(stat, i) in data.stats" :key="i">
            <div class="text-2xl font-extrabold">{{ stat.value }}</div>
            <div class="uppercase text-sm">{{ stat.label }}</div>
          </div>
        </div>
        <div class="space-y-2.5">
          <p class="uppercase font-bold text-gray-low">Ils réutilisent les données de data.gouv.fr</p>
          <div class="grid grid-cols-2 sm:grid-cols-4 justify-between">
            <img
              v-for="(partner, i) in data.partners"
              :key="i"
              class="size-20 grayscale opacity-80 object-contain"
              :src="partner.src"
              :alt="partner.alt"
            />
          </div>
        </div>
        <div class="flex flex-col sm:flex-row items-center gap-4">
          <a :href="data.link.url" class="fr-btn">{{ data.link.label }}</a>
          <a :href="data.cta.url" class="fr-btn fr-btn--secondary">
            {{ data.cta.label }}
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted, defineProps } from 'vue'

const props = defineProps<{ source: string }>()

const data = ref({
  title: '',
  description: '',
  stats: [],
  partners: [],
  link: { label: '', url: '' },
  cta: { label: '', url: '' }
})

onMounted(async () => {
  const res = await fetch('/' + props.source)
  data.value = await res.json()
})
</script>
```

---

### 3. home.yaml

```yaml
- title: Réutilisations
  reuse_community_section:
    enabled: true
    source: culture/data/reuses.json
```

---

### 4. Intégration dans `HomeView.vue`

```ts
import ReuseCommunitySection from '@/custom/culture/components/ReuseCommunitySection.vue'
```

Dans le template :

```vue
<ReuseCommunitySection
  v-if="item.reuse_community_section?.enabled"
  :source="item.reuse_community_section.source"
/>
```

---

## Bonnes pratiques

- Organiser les composants spécifiques à la transversale dans `custom/culture/components/`

---

