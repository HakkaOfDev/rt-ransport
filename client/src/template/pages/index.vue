<template>
  <div class='main'>
    <div class='header-container w-full'>
      <div class='flex flex-col h-full justify-center items-center'>
        <div class='w-full mx-auto items-center justify-center flex flex-col text-center'>
          <h1 class='header-text text-3xl lg:text-6xl text-red-500'>RT<span class='font-extrabold'>'ransport</span></h1>
          <hr class='w-20 h-1 mb-1 bg-white border-transparent' />
          <h2 class='header-text text-xl lg:text-3xl font-bold text-blue-600'>{{ $t('transport_revolution') }}</h2>
          <div class='flex flex-row justify-between items-center mt-4'>
            <label>
              <input :placeholder="$t('colis_research')"
                     class='w-64 pl-2.5 sm:text-sm lg:text-lg rounded-full border bg-gray-100 focus:border-gray-900 border-transparent outline-none border- focus:bg-white p-1'
                     type='search' />
            </label>
            <a class='ml-1 text-base leading-6 font-medium text-xl bg-red-500 hover:bg-red-400 text-white rounded-full p-2 transition ease-in-out duration-150 cursor-pointer'
               type='submit'>
              <span class="icon-search"></span>
            </a>
          </div>
        </div>
      </div>
    </div>
    <div class='w-full h-6 flex justify-center flex-col items-center'>
      <span class='icon-arrow-down2 animate-bounce text-5xl text-red-500 cursor-pointer'/>
    </div>
  </div>
</template>

<script lang='ts'>
import Vue from 'vue'

export default Vue.extend({
  layout: 'master'
})
</script>

<style lang='scss' src='./index.scss'></style>