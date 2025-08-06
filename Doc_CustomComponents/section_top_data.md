# 🔥 Découvrez les données phares
ID : section_top_data

## Objectif
Mettre en valeur les jeux de données les plus consultés sur la plateforme, afin d’encourager l’exploration des ressources jugées pertinentes ou utiles par la communauté. Ce bloc permet de valoriser les données à fort impact et d'orienter les utilisateurs vers les contenus les plus visités.

## Automatisation
Automatisé, les liens des cards sont des requêtes de l'API avec un tri dynamique selon nombre de vues, réutilisations

## Périodicité d’actualisation
Actualisation dynamique


## Contenu
- titre de la section : 
- chaque carte présente :
    - le titre : exeemple "Découvrez les données phares"
    - une image (disponible au sein du répertoire asset
    - une description (description)
    - Redirection vers résultats de la requête API


## Composant DSFR :  

Type : Card ou Card contenu enrichi
Style : fr-card, fr-card--horizontal, fr-card—sm

## Spécifications des cards

| Élément                  | Emoji | Requête API        | Nombre | Objectif                                               |
| :----------------------- | :---- | :----------------- | :----- | :----------------------------------------------------- |
| Jeux les plus consultés  | 🔥    | `sort=-views`      | 20     | Mettre en avant les contenus les plus populaires       |
| Jeux les plus réutilisés | ♻️    | `sort=-reuses`     | 20     | Valoriser les jeux fréquemment repris ou remixés       | 
| Nouveaux jeux publiés    | 🆕    | `sort=-created_at` | 20     | Montrer les dernières publications de données ouvertes | 




## Mise en pratique
### Code Yaml
```
- title: Découvrez les données phares
  id: section_top_data
  content:
    sub_section_datasets:
    sub_section_cards:
      title:
      cards:
        - name: '🔥 Jeux les plus consultés'
          description: 'Découvrez les jeux les plus populaires sur la plateforme, en fonction du nombre de vues.'
          url: 'datasets?sort=-views'
          image_url: '/culture/assets/patrimoine.png'
        - name: '♻️ Jeux les plus réutilisés'
          description: 'Explorez les jeux de données les plus réutilisés par la communauté.'
          url: 'datasets?sort=-reuses'
          image_url: '/culture/assets/audiovisuel.png'
        - name: '🆕 Nouveaux jeux publiés'
          description: 'Parcourez les nouveaux jeux de données publiés sur la plateforme.'
          url: 'datasets?sort=-created_at'
          image_url: '/culture/assets/musee.png'
    sub_section_tiles:
    sub_section_buttons:
```
### Liste des requêtes, les résultats sont stockés au sein du repertoire /public/culture/data/

* views.json : Requête 1 : https://www.data.gouv.fr/api/1/datasets/?organization=534fff91a3a7292c64a77f73&sort=-views&page=1&page_size=10
* reuses.json : Requête 2 : https://www.data.gouv.fr/api/1/datasets/?organization=534fff91a3a7292c64a77f73&sort=-reuses&page=1&page_size=10
* created_at.json : Requête 3 : https://www.data.gouv.fr/api/1/datasets/?organization=534fff91a3a7292c64a77f73&sort=-created_at&page=1&page_size=10

### Déclaration section Yaml
```
      - title: Explorer les données culturelles
        id: section_explorer_data
        content:
        section_explorer_cards:
          title: "Explorer les données culturelles"
          cards:
            - name: "🔥 Jeux les plus consultés"
              description: "Découvrez les jeux les plus populaires sur la plateforme."
              url: "datasets?sort=-views"
              image_url: "/culture/assets/patrimoine.png"
              source: "https://raw.githubusercontent.com/datagouv/portail-culture/refs/heads/Documentation/data/views.json"
              limit: 5

            - name: "♻️ Jeux les plus réutilisés"
              description: "Explorez les jeux de données les plus réutilisés par la communauté."
              url: "datasets?sort=-reuses"
              image_url: "/culture/assets/audiovisuel.png"
              source: "https://raw.githubusercontent.com/datagouv/portail-culture/refs/heads/Documentation/data/reuses.json"
              limit: 5

            - name: "🆕 Nouveaux jeux publiés"
              description: "Parcourez les nouveaux jeux de données publiés sur la plateforme."
              url: "datasets?sort=-created_at"
              image_url: "/culture/assets/musee.png"
              source: "https://raw.githubusercontent.com/datagouv/portail-culture/refs/heads/Documentation/data/created.json"
              limit: 5

```
### custom composant section 
```
<template>
  <section class="fr-container fr-py-6w">
    <h2 class="fr-h3">{{ heading }}</h2>
    <div class="fr-grid-row fr-grid-row--gutters">
      <div
        v-for="(card, i) in cards"
        :key="i"
        class="fr-col-12 fr-col-md-6 fr-col-lg-4"
      >
        <!-- ⚡ suppression de fr-enlarge-link -->
        <div class="fr-card fr-card--vertical">
          <div class="fr-card__header" v-if="card.image_url">
            <div class="fr-card__img">
              <img
                class="fr-responsive-img"
                :src="card.image_url"
                :alt="card.name"
              />
            </div>
          </div>

          <div class="fr-card__body">
            <div class="fr-card__content">
              <h3 class="fr-card__title">{{ card.name }}</h3>
              <p class="fr-card__desc">{{ card.description }}</p>

              <!-- Liste des jeux de données -->
              <ul v-if="card.datasets && card.datasets.length" class="fr-mt-2w fr-links-group">
                <li
                  v-for="(dataset, j) in card.datasets.slice(0, 3)"
                  :key="j"
                >
                  <a
                    class="fr-link"
                    :href="dataset.page"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    {{ dataset.title }}
                  </a>
                </li>
              </ul>
              <p v-else class="fr-text--sm">Aucun jeu disponible pour le moment.</p>
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
  cards: {
    name: string
    description: string
    url: string
    image_url: string
    source?: string
    limit?: number
    datasets?: { title: string; page: string }[]
  }[]
}>()

const cards = ref([...props.cards])

onMounted(async () => {
  await Promise.all(
    cards.value.map(async (card) => {
      if (card.source) {
        try {
          const res = await fetch(card.source)
          const data = await res.json()
          card.datasets =
            data.data?.map((d: any) => ({
              title: d.title,
              page: d.url
            })) || []
        } catch (e) {
          console.warn('Erreur lors du chargement du fichier', card.source, e)
          card.datasets = []
        }
      }
    })
  )
})
</script>

<style scoped>
.fr-card__content {
  display: flex;
  flex-direction: column;
}

.fr-card__title {
  order: 0;
}
.fr-card__desc {
  order: 1;
}
.fr-links-group {
  order: 2;
  list-style: none;
  padding-left: 0;
}
.fr-links-group li {
  margin-bottom: 0.5rem;
}
</style>

```

### Etape déclaration section au sein de HomeView.vue
```
<!-- Nouveau composant custom -->
        <SectionExplorerCards
          v-if="item.section_explorer_cards"
          :heading="item.section_explorer_cards.title"
          :cards="item.section_explorer_cards.cards"
        />

```

```
import SectionExplorerCards from '@/custom/culture/customComponents/SectionExplorerCards.vue'
```


