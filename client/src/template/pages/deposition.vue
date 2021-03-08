<template>
  <div class='main'>
    <div class='w-full h-screen flex flex-row justify-center items-start space-y-3 text-center'>
      <div class='text-center'>
        <h1 class='text-3xl my-3'>Déposition</h1>
        <form id='deposition' class='flex flex-col justify-center items-center space-y-3'>
          <div class='flex flex-row justify-between items-center space-x-2'>
            <span class='icon-crop'></span>
            <label>
              <input placeholder="H"
                     class='w-16 text-lg border bg-gray-100 rounded-full focus:border-gray-900 border-transparent outline-none border- focus:bg-white py-0.25 px-1.5'
                     type='text' />
            </label>
            <p>x</p>
            <label>
              <input placeholder="L"
                     class='w-16 text-lg border bg-gray-100 rounded-full focus:border-gray-900 border-transparent outline-none border- focus:bg-white py-0.25 px-1.5'
                     type='text' />
            </label>
            <p>x</p>
            <label>
              <input placeholder="P"
                     class='w-16 text-lg border bg-gray-100 rounded-full focus:border-gray-900 border-transparent outline-none border- focus:bg-white py-0.25 px-1.5'
                     type='text' />
            </label>
            <p>en cm</p>
          </div>
          <div class='flex flex-row justify-between items-center space-x-2'>
            <span class='icon-download3'></span>
            <label>
              <input :placeholder="$t('parcel_weight')"
                     class='w-20 text-lg border bg-gray-100 rounded-full focus:border-gray-900 border-transparent outline-none border- focus:bg-white py-0.25 px-1.5'
                     type='text' />
            </label>
            <p>en kg</p>
          </div>
          <label class='flex flex-row justify-between items-center space-x-2'>
            <span class='icon-spinner4'></span>
            <p>Emballage</p>
            <select class='w-full border bg-white rounded px-3 py-2 outline-none w-full'>
              <option class='py-1'>Carton</option>
              <option class='py-1'>Polystyrène</option>
              <option class='py-1'>Papier</option>
            </select>
          </label>
          <div class='flex flex-row justify-between items-center space-x-2'>
            <label>
              <input type='checkbox' v-model='form.assured' />
              Assuré
            </label>
            <div class='' v-if='form.assured'>
              <select class='w-full border bg-white rounded px-3 py-2 outline-none w-full'>
                <option class='py-1' disabled selected>Type d'assurance</option>
                <option class='py-1'>15$ - Niveau 2</option>
                <option class='py-1'>5$ - Niveau 1</option>
              </select>
            </div>
          </div>
          <label>
            <input type='checkbox' />
            Fragile
          </label>
          <button
            class='text-lg rounded-full bg-red-500 hover:bg-red-400 text-white py-1 px-2.5 border-transparent cursor-pointer'
            type='submit'
            @click.prevent=''>
            {{ $t('submit') }}
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script lang='ts'>
import Vue from 'vue'

export default Vue.extend({
  layout: 'master',
  data() {
    return {
      form: {
        assured: false
      }
    }

  }
})
</script>

<style lang='scss' src='./index.scss'></style>