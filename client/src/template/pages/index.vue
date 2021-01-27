<template>
	<div class="main">
		<div class="header-container w-full">
			<div class="flex flex-col h-full justify-center items-center">
				<div class="w-full mx-auto items-center justify-center flex flex-col text-center">
					<h1 class="header-text text-3xl lg:text-6xl font-extrabold text-red-500">RT'ransport</h1>
					<hr class="w-20 h-1 mb-1 bg-white border-transparent"/>
					<h2 class="header-text text-xl lg:text-3xl font-bold text-blue-600">{{ $t('transport_revolution') }}</h2>
					<div class="flex flex-row justify-between items-center mt-4">
						<label>
							<input type="search" class="w-64 sm:text-sm lg:text-lg rounded-full border bg-gray-100 focus:border-gray-900 border-transparent outline-none border- focus:bg-white p-1" :placeholder="$t('colis_research')"  />
						</label>
						<a type="submit" class="ml-1 text-base leading-6 font-medium text-xl bg-red-500 hover:bg-red-400 text-white rounded-full p-2 transition ease-in-out duration-150 cursor-pointer">
							<fa :icon="['fas', 'search']"/>
						</a>
					</div>
				</div>
			</div>
		</div>
		<div class="w-full h-6 flex justify-center flex-col items-center">
			<fa class="animate-bounce text-5xl text-red-500" :icon="['fas', 'arrow-down']"/>
		</div>
	</div>
</template>

<script>
export default {
	layout: 'master',
}
</script>

<style lang="scss" src="./index.scss"></style>
