<template>
  <main>
    <div class='block h-auto py-5 px-20 w-full'>
      <div class='flex flex-row justify-center items-center space-x-10 w-full'>
        <div class='flex flex-col justify-end items-end space-y-2 w-1/2'>
          <label class='space-x-2'>
            <span>Pseudo</span>
            <span class='icon-user'></span>
            <input placeholder='John'
                   class='w-96 pl-2.5 text-lg border bg-gray-100 focus:border-gray-900 border-transparent outline-none border-transparent focus:bg-white p-1'
                   type='text' />
          </label>
          <label class='space-x-2'>
            <span>Email</span>
            <span class='icon-at'></span>
            <input placeholder='john.doe@gmail.com'
                   class='w-96 pl-2.5 text-lg border bg-gray-100 focus:border-gray-900 border-transparent outline-none border-transparent focus:bg-white p-1'
                   type='email' />
          </label>
          <label class='space-x-2'>
            <span>Message</span>
            <span class='icon-bubble2'></span>
            <textarea placeholder='John'
                      class='w-96 pl-2.5 text-lg border bg-gray-100 focus:border-gray-900 border-transparent outline-none border-transparent focus:bg-white p-1'
                      rows='3' minlength='3' maxlength='5' />
          </label>
          <button class='text-lg justify-center rounded-full bg-red-500 hover:bg-red-400 text-white p-1 px-2.5 border-transparent cursor-pointer' type='submit'
                  @click.prevent=''>
            {{ $t('submit') }}
          </button>
        </div>
        <div class='w-1/2 p-10 flex flex-col justify-center items-center'>
          <div class='text-left shadow-lg h-auto p-10 w-10/12 space-y-3'>
            <h3 class='text-2xl text-red-500 font-bold uppercase'>{{ $t('become_supplier_title') }}</h3>
            <hr class='w-1/4 h-1 bg-blue-600'/>
            <p class='text-base text-lg'>{{ $t('become_supplier_content') }}</p>
          </div>
          <div class='text-left shadow-lg h-auto  p-10 w-10/12 space-y-3'>
            <h3 class='text-2xl text-red-500 font-bold uppercase'>{{ $t('become_operator_title') }}</h3>
            <hr class='w-1/4 h-1 bg-blue-600'/>
            <p class='text-base text-lg'>{{ $t('become_operator_content') }}</p>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  layout: 'master',
  data() {
    return {
      form: {
        email: '',
        password: ''
      }
    }

  },
  methods: {
    handleLogin: async function() {
      if (this.form.email !== '' && this.form.password !== '') {
        let data = new FormData()
        data.append('email', this.form.email)
        data.append('password', this.form.password)
        console.log(data)
        let response = await this.$axios.post('/users/login', data, { 'Content-Type': 'application/json' })
        console.log(response)
      }
    }
  }
}
</script>

<style lang='scss' scoped>

</style>
