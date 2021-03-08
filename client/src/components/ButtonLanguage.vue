<template>
  <div
    class='fixed bottom-28 md:bottom-4 right-4 z-50 bg-red-500 h-12 w-12 rounded-full transition ease-in-out duration-150 hover:bg-red-400'>
    <div
      :text='$i18n.locale.toUpperCase()'
      class='absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2'
    >
      <div
        v-for='(lang, key) in availableLocales'
        :key='key'
        class='text-white text-xl font-medium cursor-pointer'
        @click.prevent='changeLanguage(lang.code)'
      >
        {{ lang.code.toUpperCase() }}
      </div>
    </div>
  </div>
</template>

<script lang='ts'>
import { defineComponent } from '@nuxtjs/composition-api'
import { useButton } from '@/services/useTranslation'

export default defineComponent({
  name: 'ButtonLanguageVue',
  setup() {
    const { availableLocales, changeLanguage } = useButton()
    return {
      availableLocales,
      changeLanguage
    }
  }
})
</script>

<style scoped></style>
