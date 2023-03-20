<template>
    <div class="column is-3">
        <div class="box">
            <figure class="image">
                <img v-bind:src="dish.get_image" alt="image">
            </figure>

            <h3 class="is-size-4">{{ dish.name }}</h3>
            <p class="is-size-6 has-text-grey">${{ dish.price }}</p>

            <router-link v-bind:to="dish.get_absolute_url" class="button is-info is-light mt-4">View details</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: 'DishBox',
    props: {
        dish: Object
    }
}
</script>

<style scoped>
.image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
}

.box {
    border-radius: 10px 10px 0 0;
}

img {
    border-radius: 10px 10px 0 0;
}
</style>