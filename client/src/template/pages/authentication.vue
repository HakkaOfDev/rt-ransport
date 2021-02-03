<template>
	<div class="main">
		<div class="w-full h-64 flex flex-row justify-center items-center space-y-3">
			<div class="login">
				<h1>{{ $t('auth_title') }}</h1>
				<form class="flex flex-col justify-center items-center space-y-3">
					<div class="flex flex-row justify-between items-center space-x-2">
						<fa :icon="['fas', 'at']"/>
						<label>
							<input type="text" v-model="form.email" class="w-64 text-lg border bg-gray-100 rounded-full focus:border-gray-900 border-transparent outline-none border- focus:bg-white p-1" :placeholder="$t('auth_user')"/>
						</label>
					</div>
					<div class="flex flex-row justify-between items-center space-x-2">
						<fa :icon="['fas', 'key']"/>
						<label>
							<input type="password" v-model="form.password" class="w-64 text-lg border bg-gray-100 rounded-full focus:border-gray-900 border-transparent outline-none border- focus:bg-white p-1" :placeholder="$t('auth_password')"/>
						</label>
					</div>
					<button type="submit" @click.prevent="handleLogin" class="text-lg rounded-full bg-red-500 hover:bg-red-400 text-white p-1 border-transparent cursor-pointer">{{ $t('submit') }}</button>
				</form>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	layout: 'master',
	data() {
		return {
			form: {
				email: "",
				password: ""
			}
		}

	},
	methods: {
		handleLogin: async function() {
			if(this.form.email !== "" && this.form.password !== "") {
				let data = new FormData();
				data.append("email", this.form.email)
				data.append("password", this.form.password)
				console.log(data)
				let response = await this.$axios.post("/users/login", data, { 'Content-Type': 'application/json' });
				console.log(response)
			}
		}
	},
}
</script>

<style lang="scss" scoped>

</style>
