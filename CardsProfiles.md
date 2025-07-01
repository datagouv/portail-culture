# Intégration de section en HTML directement au seim du Yaml

Exemple 
```
- title:
        content: >-
          <h2 class="fr-h1 fr-mt-15w fr-mb-5w" style="color: black; text-align: center;">Améliorer les services à destination :</h2>

          <p class="fr-text--lg" style="text-align: center;">
          Le portail <i>simplifions.data.gouv.fr</i> vous accompagne pour simplifier, avec de la donnée, les démarches des citoyens.<br/>Retrouvez tous les cas d'usages selon le public concerné :
          </p>

          <div class="fr-grid-row fr-grid-row--gutters">
          <div class="fr-col-12 fr-col-lg-3">
            <div class="fr-tile fr-tile--horizontal fr-enlarge-link" id="tile-sourcing">
            <div class="fr-tile__body">
              <div class="fr-tile__content">
              <h3 class="fr-tile__title fr-h3">
                <a href="/cas-d-usages?tags=spf-users-particuliers">Particuliers<br/>👱</a>
              </h3>
              <p class="fr-tile__detail fr-h6">Tous les cas d'usages concernant les particuliers</p>
              </div>
            </div>
            </div>
          </div>

          <div class="fr-col-12 fr-col-lg-3">
            <div class="fr-tile fr-tile--horizontal fr-enlarge-link" id="tile-sourcing">
            <div class="fr-tile__body">
              <div class="fr-tile__content">
              <h3 class="fr-tile__title fr-h3">
                <a href="/cas-d-usages?tags=spf-users-entreprises">Entreprises<br/>💼</a>
              </h3>
              <p class="fr-tile__detail fr-h6">Tous les cas d'usages concernant les entreprises</p>
              </div>
            </div>
            </div>
          </div>

          <div class="fr-col-12 fr-col-lg-3">
            <div class="fr-tile fr-tile--horizontal fr-enlarge-link" id="tile-sourcing">
            <div class="fr-tile__body">
              <div class="fr-tile__content">
              <h3 class="fr-tile__title fr-h3">
                <a href="/cas-d-usages?tags=spf-users-associations">Associations<br/>🤝</a>
              </h3>
              <p class="fr-tile__detail fr-h6">Tous les cas d'usages concernant les associations</p>
              </div>
            </div>
            </div>
          </div>

          <div class="fr-col-12 fr-col-lg-3">
            <div class="fr-tile fr-tile--horizontal fr-enlarge-link" id="tile-sourcing">
            <div class="fr-tile__body">
              <div class="fr-tile__content">
              <h3 class="fr-tile__title fr-h3">
                <a href="/cas-d-usages?tags=spf-users-agents-publics">Agents publics<br/>🧑‍💼</a>
              </h3>
              <p class="fr-tile__detail fr-h6">Tous les cas d'usages concernant les agents publics</p>
              </div>
            </div>
            </div>
          </div>

          </div>
        sub_section_buttons:
          - name: "Tous les cas d'usages"
            url: 'cas-d-usages'
            class: 'fr-btn fr-btn--icon-left fr-btn--lg fr-icon-checkbox-circle-fill'
```
