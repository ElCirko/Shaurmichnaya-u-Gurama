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

      <div class="column is-3" v-for="dish in latestDishes" v-bind:key="dish.id">
        <div class="box">
          <figure class="image">
            <img v-bind:src="dish.get_image">
          </figure>

          <h3 class="is-size-4"> {{ dish.name }} </h3>
          <p class="is-size-6 has-text-grey">${{ dish.price }}</p>

          View details
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomeView',

  data() {
    return {
      latestDishes: []
    }
  },
  components: {
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
