<template>
  <div class="home">
    <section class="hero is-small is-warning mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to Shawa u Gurama
        </p>
        <p class="subtitle">
          The best shawarma store online
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest dishes</h2>
      </div>

      <DishBox v-for="dish in latestDishes" v-bind:key="dish.id" v-bind:dish="dish"></DishBox>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
import DishBox from "@/components/DishBox.vue";


export default {
  name: 'HomeView',

  data() {
    return {
      latestDishes: []
    }
  },
  components: {
    DishBox
  },

  mounted() {
    this.getLatestDishes()
  },
  
  methods: {
    getLatestDishes() {
      axios
        .get('/api/latest-dishes/')
        .then(response => {
          this.latestDishes = response.data
          console.log(this.latestDishes)
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}
</style>
