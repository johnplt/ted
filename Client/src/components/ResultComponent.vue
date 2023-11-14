<template>
  <div>
    <DsfrSearchBar
      v-model="searchQuery"
      placeholder="Data Scientist"
      @search="performSearch"
    />
    <div v-if="searchPerformed" >
    <label v-for="column in columnOrder" :key="column">
      <input v-model="selectedColumns" type="checkbox" :value="column" />
      {{ column }} <!-- Affichez le nom de la colonne -->
    </label>
    </div>
    <DsfrTable
      v-if="searchPerformed && filteredData.length > 0"
      class="fr-table--layout-fixed"
      title="tableau"
      :headers="orderedSelectedColumns"
      :pagination="true"
      :rows="filteredData"
      :default-current-page="defaultCurrentPage"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import jsonData from '../../donnees_offres.json'

const searchQuery = ref('')
const searchPerformed = ref(false)
const defaultCurrentPage = ref(1)
const headers = [
  'Titre du poste',
  'date de publication',
  'Ref',
  'Fonction publique',
  'Employeur',
  'Localisation',
  'Date limite de candidature',
  'Domaine',
  'Nature emploi',
  'Expérience souhaitée',
  'Rémunération',
  'Catégorie',
  'Management',
  'Télétravail possible',
  'information mission',
  'profil recherché',
  'niveau',
  'Qui sommes nous?',
  'Informations complémentaires',
  'Conditions particulières d’exercice',
  'Métier de référence',
  'Fondement juridique',
  'Statut du poste',
  'Url Offre',
  'Adresse email',
]
const data = ref([])
const selectedColumns = ref(['Titre du poste'])
const columnOrder = ref([...headers])

onMounted(() => {
  data.value = jsonData
})

// Utilisez computed pour appliquer les filtres aux données
const filteredData = computed(() => {
  const query = searchQuery.value.toLowerCase().trim()
  return data.value
    .filter((item) => {
      // Filtrez les données en fonction du mot-clé dans toutes les colonnes
      return (
        query === '' ||
        Object.values(item).some((value) => {
          return value && typeof value === 'string' && value.toLowerCase().includes(query)
        })
      )
    })
    .map((item) => {
      return Object.fromEntries(
        Object.entries(item).filter(([key]) => selectedColumns.value.includes(key)),
      )
    })
})

const orderedSelectedColumns = computed(() => {
  return columnOrder.value.filter((column) => selectedColumns.value.includes(column))
})
const performSearch = () => {
  searchPerformed.value = true
}
</script>
