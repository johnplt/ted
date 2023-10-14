
<script setup lang="ts">
import ResultComponent from '@/components/ResultComponent.vue'
import jsonData from '../../donnees_offres.json'

const data = ref([])

const totalOffers = computed(() => {
  return data.value.length
})

onMounted(() => {
  data.value = jsonData
})


</script>

<template>
  <div>
    <h1>Trouver mon expertise data</h1>
    <span> il y a  {{ totalOffers }} offres</span>
    <ResultComponent  />
  </div>
</template>
