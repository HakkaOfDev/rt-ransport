<template>
	<div class="fixed bottom-28 md:bottom-4 right-4 z-50">
		<div :text="$i18n.locale.toUpperCase()" variant="primary" class="relative bg-red-500 hover:bg-red-400 transition-all duration-300 w-12 h-12 rounded-full shadow-lg">
			<div class="absolute inset-0 flex items-center justify-center font-bold text-white cursor-pointer" v-for="(lang, key) in availableLocales" :key="key" @click.prevent="changeLanguage(lang.code)">{{ lang.code.toUpperCase() }}</div>
		</div>
	</div>
</template>

<script>
import { useContext, computed } from '@nuxtjs/composition-api'

export default {
	setup() {
		const { store } = useContext()
		const availableLocales = computed(() => store.$i18n.locales.filter((i) => i.code !== store.$i18n.locale))
		function changeLanguage(lang) {
			store.$i18n.setLocale(lang)
		}

		return {
			availableLocales,
			changeLanguage,
		}
	},
}
</script>

<style lang="scss" scoped>
.md\:bottom-4 {
	bottom: 6rem;
	@media screen and (min-width: 768px){
		bottom: 1rem;
	}
}
.right-4 {
	right: 0.5rem;
	@media screen and (min-width: 1024px) {
		right: 1rem;
	}
}
</style>
