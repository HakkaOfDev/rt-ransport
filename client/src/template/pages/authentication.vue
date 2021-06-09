<template>
  <div class='main'>
    <div class='w-full h-64 flex flex-row justify-center items-center space-y-3'>
      <div class='login text-center'>
        <h1 class='text-3xl my-3'>{{ $t('auth_title') }}</h1>
        <form class='flex flex-col justify-center items-center space-y-3'>
          <div class='flex flex-row justify-between items-center space-x-2'>
            <span class='icon-at1 text-gray-900 text-2xl'></span>
            <label>
              <input v-model='state.email' :placeholder="$t('auth_user')"
                     class='w-64 pl-2.5 text-lg border bg-gray-100 rounded-full focus:border-gray-900 border-transparent outline-none border-transparent focus:bg-white p-1'
                     type='text' required />
            </label>
          </div>
          <div class='flex flex-row justify-between items-center space-x-2'>
            <span class='icon-key2 text-gray-900 text-2xl'></span>
            <label>
              <input v-model='state.password' :placeholder="$t('auth_password')"
                     class='w-64 pl-2.5 text-lg border bg-gray-100 rounded-full focus:border-gray-900 border-transparent outline-none border-transparent focus:bg-white p-1'
                     type='password' required />
            </label>
          </div>
          <button
            class='text-lg rounded-full bg-red-500 hover:bg-red-400 text-white p-1 px-2.5 border-transparent cursor-pointer'
            type='submit'
            @click.prevent='handleSubmit'>
            {{ $t('submit') }}
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import {useLogin} from '../../services/useAuthentication'
import {defineComponent} from '@nuxtjs/composition-api'

export default defineComponent({
  layout: 'master',
  middleware: 'auth',
  setup() {
    const { state, handleSubmit } = useLogin()
    return {
      state, handleSubmit
    }
  }
})
</script>

<style lang='scss' scoped>

</style>
