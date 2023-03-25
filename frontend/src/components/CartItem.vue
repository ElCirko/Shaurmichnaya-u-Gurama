<template>
    <tr>
        <td class="has-text-link-dark">
            <router-link :to="item.dish.get_absolute_url">{{ item.dish.name }}</router-link>
        </td>
        <td class="has-text-success">${{ item.dish.price }}</td>
        <td>
            {{ item.quantity }}
            <a class="has-background-success-light ml-2 px-2 py-1" @click="incrementQuantity(item)">➕</a>
            <a class="has-background-danger-light ml-4 px-2 py-1" @click="decrementQuantity(item)">➖</a>
        </td>
        <td class="has-text-success">${{ getItemTotal(item).toFixed(2) }}</td>
        <td>
            <button class="delete has-background-danger" @click="removeFromCart(item)"></button>
        </td>
    </tr>
</template>

<script>
export default {
    name: 'CartItem',

    props: {
        initialItem: Object
    },

    data() {
        return {
            item: this.initialItem
        }
    },

    methods: {
        getItemTotal(item) {
            return item.quantity * item.dish.price
        },
        decrementQuantity(item) {
            this.item.quantity -= 1

            if (item.quantity == 0) {
                this.$emit('removeFromCart', item)
            }

            this.updateCart()
        },

        incrementQuantity(item) {
            this.item.quantity += 1

            this.updateCart()
        },

        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },

        removeFromCart(item) {
            this.$emit('removeFromCart', item)

            this.updateCart()
        }
    }
}
</script>