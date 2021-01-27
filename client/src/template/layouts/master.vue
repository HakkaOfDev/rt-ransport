<template>
	<div>
		<Navbar/>
		<NavResponsive/>
		<client-only>
			<LangSwitcher />
		</client-only>
		<Nuxt />
	</div>
</template>

<script>
import LangSwitcher from '~/components/LangSwitcher'
import Navbar from '~/components/navbar/navbar';
import NavResponsive from "~/components/responsivenav/NavResponsive";

export default {
	name: 'master',
	components: { NavResponsive, Navbar, LangSwitcher },
}
</script>

<style lang="scss" scoped>
body {
	width: 100%;
	min-height: 100%;
}
</style>
