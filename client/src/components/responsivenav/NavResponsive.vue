<template>
  <div class='md:hidden fixed z-50 bottom-0 w-full flex justify-between bg-white shadow-reverse' style='height: 10vh;'>
    <a class='relative w-full h-full ' href='/'>
      <div class='item'>
        <span class="icon-home text-gray-900 text-2xl"></span>
        <span class='text-gray-900 uppercase text-sm'>{{ $t('home_nav_title') }}</span>
      </div>
    </a>
    <a class='relative w-full h-full ' href='/prices'>
      <div class='item'>
        <span class="icon-coin-dollar text-gray-900 text-2xl"></span>
        <span class='text-gray-900 uppercase text-sm'>{{ $t('tariff_nav_title') }}</span>
      </div>
    </a>
    <a class='relative w-full h-full' href='/my-parcels'>
      <div class='item'>
        <span class="icon-codepen text-gray-900 text-2xl"></span>
        <span class='text-gray-900 uppercase text-sm'>{{ $t('parcels_nav_title') }}</span>
      </div>
    </a>
    <a class='relative w-full h-full ' href='/contact'>
      <div class='item'>
        <span class="icon-bubbles4 text-gray-900 text-2xl"></span>
        <span class='text-gray-900 uppercase text-sm'>Contact</span>
      </div>
    </a>
  </div>
</template>

<script>
export default {
  name: 'NavResponsive'
}
</script>

<style lang='scss' src='./NavResponsive.scss'></style>
