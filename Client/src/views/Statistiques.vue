<script setup lang="ts">
import jsonData from '../../donnees_offres.json'
import { ref, computed, onMounted } from 'vue'

const data = ref([])

const geographicDistribution = ref([])
const calculateGeographicDistribution = () => {
  // Assurez-vous d'avoir des données dans "data" avant de calculer la répartition
  if (data.value.length > 0) {
    // Créez la répartition géographique
    const cityCount = data.value.reduce((cityMap, offer) => {
      const city = offer.Localisation

      if (!cityMap[city]) {
        cityMap[city] = 1
      } else {
        cityMap[city]++
      }

      return cityMap
    }, {})

    // Triez les villes par nombre d'offres décroissant
    const sortedCities = Object.keys(cityCount).sort((a, b) => cityCount[b] - cityCount[a])

    // Créez un tableau d'objets de répartition géographique
    const distribution = sortedCities.map((city) => ({
      city,
      count: cityCount[city],
    }))

    // Mettez à jour la répartition géographique
    geographicDistribution.value = distribution
  }
}

const metiersDeReference = ref([])
const topMetiers = computed(() => {
  // Comptez les occurrences de chaque métier de référence
  const metierCounts = {}
  for (const offre of metiersDeReference.value) {
    if (!metierCounts[offre]) {
      metierCounts[offre] = 0
    }
    metierCounts[offre]++
  }

  // Triez les métiers par nombre d'offres décroissant
  const sortedMetiers = Object.keys(metierCounts).map(metier => ({
    metier,
    count: metierCounts[metier],
  }))
  sortedMetiers.sort((a, b) => b.count - a.count)

  // Sélectionnez les 10 premiers métiers les plus demandés
  return sortedMetiers.slice(0, 10)
})

// Fonction pour effectuer la statistique
const calculateFunctionStatistics = () => {
  // Assurez-vous d'avoir des données dans "data.value"
  if (data.value.length === 0) {
    return;
  }

  // Comptez le nombre d'offres pour chaque catégorie de la fonction publique
  const statistics = {};
  for (const offer of data.value) {
    const functionCategory = offer['Fonction publique'];
    if (functionCategory) {
      if (!statistics[functionCategory]) {
        statistics[functionCategory] = 1;
      } else {
        statistics[functionCategory]++;
      }
    }
  }

  // Statistiques disponibles sous forme d'objet
  return statistics
}

const functionStatistics = computed(() => calculateFunctionStatistics())

const totalJobCount = computed(() => data.value.length);

// Fonction pour calculer le nombre d'offres d'emploi avec télétravail
const calculateTelecommuteJobCount = () => {
  if (data.value.length === 0) {
    return 0;
  }

  let telecommuteCount = 0;

  for (const offer of data.value) {
    const telecommuteValue = offer['Télétravail possible'];

    if (telecommuteValue && (telecommuteValue.toLowerCase() === 'oui' || telecommuteValue.toLowerCase() === 'non')) {
      telecommuteCount++;
    }
  }

  return telecommuteCount;
};

const telecommuteJobCount = computed(() => calculateTelecommuteJobCount());

// Calcul du pourcentage d'offres d'emploi avec télétravail
const telecommutePercentage = computed(() => {
  const total = totalJobCount.value;
  if (total === 0) {
    return 0;
  }
  return (telecommuteJobCount.value / total) * 100
});

onMounted(() => {
  data.value = jsonData
  metiersDeReference.value = jsonData.map(offre => offre['Métier de référence'])
  calculateGeographicDistribution()
})

</script>
<template>
  <h1>Statistiques</h1>

  <h3>Répartition géographique des offres d'emploi</h3>
      <ul>
        <li v-for="cityData in geographicDistribution" :key="cityData.city">
          {{ cityData.city }}: {{ cityData.count }} offres
        </li>
      </ul>
  <h3>Métiers de Référence les Plus Demandés</h3>
    <div v-if="topMetiers.length > 0">
      <ul>
        <li v-for="metier in topMetiers" :key="metier.metier">
          {{ metier.metier }} - {{ metier.count }} offres
        </li>
      </ul>
    </div>
    <div v-else>
      Aucune donnée disponible.
    </div>

  <h3>Répartitions des offres sur la Fonction publique</h3>

    <div>
      <ul>
        <li v-for="(count, category) in functionStatistics" :key="category">
          {{ category }} : {{ count }} offres
        </li>
      </ul>
    </div>

  <h3>Statistique sur le Télétravail</h3>
    <p>Nombre d'offres d'emploi avec télétravail : {{ telecommuteJobCount }}</p>
    <p>Pourcentage d'offres d'emploi avec télétravail : {{ telecommutePercentage.toFixed(2) }}%</p>
</template>
