<template>
  <div class="wrapper">
    <nav class="navbar is-transparent">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <strong>U Gurama</strong>
          <img src="@/assets/logo.svg" alt="shawarma">
        </router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu"
          @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{ 'is-active': showMobileMenu }">
        <div class="navbar-start">

          <router-link to="/shawarma" class="navbar-item">Shawarma</router-link>
          <router-link to="/drinks" class="navbar-item">Drinks</router-link>
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons is-centered">
              <router-link to="/cart" class="button is-primary">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart ({{ cartTotalLength }})</span>
              </router-link>
              <router-link to="/log-in" class="button is-light">Log in</router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </div>
  <router-view />
  <footer class="footer has-background-white-bis">
    <div class="content has-text-centered">
      <p>Shawaright (c) 2023</p>
    </div>
  </footer>
</template>

<script>
export default {
  data() {
    return {
      showMobileMenu: false,
    }
  },
}
</script>

<style lang="scss">
@import '../node_modules/bulma'
</style>
