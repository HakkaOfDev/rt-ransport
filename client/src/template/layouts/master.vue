<template>
  <div>
    <Navbar />
    <NavResponsive />
    <Nuxt />
    <Footer />
    <ButtonLanguage />
  </div>
</template>

<script lang='ts'>
import { defineComponent } from '@vue/composition-api'
import ButtonLanguageVue from '@/components/ButtonLanguage.vue'
import Footer from '@/components/footer/Footer.vue'
import Navbar from '@/components/navbar/Navbar.vue'
import NavResponsive from '@/components/responsivenav/NavResponsive.vue'

export default defineComponent({
  name: 'master',
  components: { ButtonLanguage: ButtonLanguageVue, Navbar, NavResponsive, Footer }
})
</script>

<style lang='scss' scoped>
body {
  width: 100%;
  min-height: 100%;
}
</style>
