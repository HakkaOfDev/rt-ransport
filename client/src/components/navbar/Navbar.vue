<template>
  <div class='sticky bg-white shadow-md md:shadow-none border-none md:border-b lg:px-20 top-0 z-50 w-screen'>
    <div class='mx-auto px-4 sm:px-6'>
      <div
        class='flex justify-between items-center border-b-2 border-gray-100 py-5 lg:justify-center md:justify-start md:space-x-10'>
        <div class='lg:w-0 lg:flex-1'>
          <a class='flex' href='/'>
            <img alt='Logo' class='lg:h-12 w-auto sm:h-6' src='@/public/images/logo2.png'>
          </a>
        </div>
        <nav class='hidden md:flex space-x-10'>
          <a class='text-base leading-6 font-medium text-gray-800 hover:text-red-500 focus:outline-none focus:text-red-500 transition ease-in-out duration-150'
             href='/'>
            <span class="icon-home"></span>
            {{ $t('home_nav_title') }}
          </a>
          <a class='text-base leading-6 font-medium text-gray-800 hover:text-red-500 focus:outline-none focus:text-red-500 transition ease-in-out duration-150'
             href='/prices'>
            <span class="icon-coin-dollar"></span>
            {{ $t('tariff_nav_title') }}
          </a>
          <a class='text-base leading-6 font-medium text-gray-800 hover:text-red-500 focus:outline-none focus:text-red-500 transition ease-in-out duration-150'
             href='/my-parcels'>
            <span class="icon-codepen"></span>
            {{ $t('parcels_nav_title') }}
          </a>
        </nav>
        <div class='hidden md:flex items-center justify-end space-x-3 md:flex-1 lg:w-0'>
          <form class='flex flex-column items-center justify-center mr-4'>
            <label>
              <input :placeholder="$t('colis_research')"
                     class='w-48 pl-2.5 text-sm rounded-full border bg-gray-100 focus:border-gray-900 border-transparent outline-none border- focus:bg-white p-1'
                     type='search' />
            </label>
            <a class='ml-1 text-base leading-6 font-medium text-xl text-gray-800 hover:text-red-500 focus:outline-none focus:text-red-500 transition ease-in-out duration-150 cursor-pointer'
               type='submit'>
              <span class="icon-search"></span>
            </a>
          </form>
          <a class='text-base leading-6 font-medium text-2xl text-gray-800 hover:text-red-500 focus:outline-none focus:text-red-500 transition ease-in-out duration-150'
             href='/authentication'>
            <span class="icon-user"></span>
          </a>
          <a class='whitespace-no-wrap inline-flex items-center justify-center px-4 py-2 border border-transparent text-base leading-6 font-medium rounded-full text-white bg-red-500 hover:bg-red-400 focus:outline-none focus:border-indigo-700 focus:shadow-outline transition ease-in-out duration-150'
             href='/contact'>Contact</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style lang='scss' src='./Navbar.scss'></style>
