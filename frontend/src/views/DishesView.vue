<template>
    <div class="page-category">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title is-1 has-text-centered"> Shawarma list </h1>
            </div>

            <DishBox v-for="dish in dishes" v-bind:key="dish.id" v-bind:dish="dish">
            </DishBox>
        </div>
    </div>
</template>


<script>
import axios from "axios";
import DishBox from "@/components/DishBox.vue";

export default {
    name: 'DishesView',
    components: {
        DishBox
    },

    data() {
        return {
            dishes: []
        }
    },
    mounted() {
        this.getDishes()
    },

    methods: {
        async getDishes() {
            // this.$store.commit('setIsLoading', true)
            await axios
                .get(`/api/dishes/`)
                .then(response => {
                    this.dishes = response.data
                    console.log(this.dishes)
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