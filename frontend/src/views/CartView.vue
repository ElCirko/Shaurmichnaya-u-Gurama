<template>
    <div class="page-cart">
        <div class="columns is-multiline">
            <div class="column is-12 has-text-centered">
                <h1 class="title">Cart</h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth" v-if="cartTotalLength">
                    <thead>
                        <tr>
                            <th>Dish</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <CartItem v-for="item in cart.items" v-bind:key="item.dish.id" v-bind:initialItem="item"
                            v-on:removeFromCart="removeFromCart">
                        </CartItem>
                    </tbody>
                </table>

                <p v-else>You dont have any products in your cart</p>
            </div>

            <div class="column is12 box">
                <h2 class="subtitle">Summary</h2>

                <strong class="has-text-success">${{ cartTotalPrice.toFixed(2) }}</strong>, {{ cartTotalLength }} items

                <hr>

                <router-link to="/cart/checkout" class="button is-warning">Proceed to checkout</router-link>
            </div>
        </div>
    </div>
</template>

<script>
import CartItem from "@/components/CartItem";

export default {
    name: 'CartView',
    components: {
        CartItem
    },
    data() {
        return {
            cart: {
                items: []
            }
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
    },
    methods: {
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter(i => i.dish.id !== item.dish.id)
        }
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.dish.price * curVal.quantity
            }, 0)
        },
    }
}
</script>