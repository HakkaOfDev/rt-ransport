<template>
	<div class="md:hidden fixed z-50 bottom-0 w-full flex justify-between bg-white shadow-reverse" style="height: 10vh;">
		<a href="/" class="relative w-full h-full ">
			<div class="item">
				<fa class="text-gray-900 text-2xl" :icon="['fas', 'home']"/>
				<span class="text-gray-900 uppercase text-sm">{{ $t('home_nav_title') }}</span>
			</div>
		</a>
		<a href="/achievements" class="relative w-full h-full ">
			<div class="item">
				<fa class="text-gray-900 text-2xl" :icon="['fas', 'dollar-sign']"/>
				<span class="text-gray-900 uppercase text-sm">{{ $t('tariff_nav_title') }}</span>
			</div>
		</a>
		<a href="/about-me" class="relative w-full h-full">
			<div class="item">
				<fa class="text-gray-900 text-2xl" :icon="['fas', 'search']"/>
				<span class="text-gray-900 uppercase text-sm">{{ $t('search_nav_title') }}</span>
			</div>
		</a>
		<a href="/contact" class="relative w-full h-full ">
			<div class="item">
				<fa class="text-gray-900 text-2xl" :icon="['fas', 'comment']"/>
				<span class="text-gray-900 uppercase text-sm">Contact</span>
			</div>
		</a>
	</div>
</template>

<script>
export default {
	name: 'NavResponsive',
}
</script>

<style lang="scss" src="./NavResponsive.scss"></style>
