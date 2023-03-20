<template>
    <section class="section">
        <div class="container">
            <div class="columns is-vcentered is-multiline ">
                <div class="column is-6-tablet is-3-desktop ">
                    <h1 class="is-size-3-mobile is-size-1-desktop title">{{ dish.name }}</h1>
                    <p>{{ dish.description }}</p>
                </div>
                <div class="column is-6-tablet is-5-desktop has-text-centered">
                    <img v-bind:src="dish.get_image" :alt="dish.name" class="px-auto">
                </div>
                <div class="column is-12-tablet is-4-desktop">
                    <div class="is-size-4 mb-2 ml-6 px-4">${{ dish.price }}</div>
                    <form>

                        <div class="field has-addons mt-2 ml-6 px-4">
                            <div class="control">
                                <input type="number" class="input is-primary is-small" min="1" v-model="quantity">
                            </div>

                            <div class="control">
                                <a class="button is-primary is-small is-outlined" @click="addToCart">Add to cart</a>
                            </div>
                        </div>

                    </form>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios';

export default {
    name: 'DishView',
    data() {
        return {
            dish: {},
            quantity: 1
        }
    },
    mounted() {
        this.getDish()
    },
    methods: {
        async getDish() {
            // this.$store.commit('setIsLoading', true)
            const slug = this.$route.params.slug
            await axios
                .get(`/api/dish/${slug}`)
                .then(response => {
                    this.dish = response.data
                    document.title = this.dish.name
                })
                .catch(error => {
                    console.log(error)
                })
            // this.$store.commit('setIsLoading', false)
        }
    }
}
</script>

<style scoped>
img {
    border-radius: 10px;
}
</style>