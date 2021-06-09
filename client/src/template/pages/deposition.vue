<template>
  <div class='main'>
    <div class='w-full h-screen flex flex-row justify-center items-start space-y-3 text-center'>
      <div class='text-center'>
        <h1 class='text-3xl my-3'>{{ $t('deposition') }}</h1>
        <form id='deposition' class='flex flex-col justify-center items-center space-y-3'>
          <div class='flex flex-row justify-between items-center space-x-2'>
            <span class='icon-user'></span>
            <label>
              <input placeholder="Customer Ref" v-model='form.customer'
                     class='w-36 text-lg border bg-gray-100 rounded-full focus:border-gray-900 border-transparent outline-none border- focus:bg-white py-0.25 px-1.5'
                     type='text' />
            </label>
          </div>
          <div class='flex flex-row justify-between items-center space-x-2'>
            <span class='icon-user'></span>
            <label>
              <input placeholder="Supplier Ref" v-model='form.supplier'
                     class='w-36 text-lg border bg-gray-100 rounded-full focus:border-gray-900 border-transparent outline-none border- focus:bg-white py-0.25 px-1.5'
                     type='text' />
            </label>
          </div>
          <div class='flex flex-row justify-between items-center space-x-2'>
            <span class='icon-crop'></span>
            <label>
              <input placeholder="H" v-model='form.height'
                     class='w-16 text-lg border bg-gray-100 rounded-full focus:border-gray-900 border-transparent outline-none border- focus:bg-white py-0.25 px-1.5'
                     type='text' />
            </label>
            <p>x</p>
            <label>
              <input placeholder="L" v-model='form.width'
                     class='w-16 text-lg border bg-gray-100 rounded-full focus:border-gray-900 border-transparent outline-none border- focus:bg-white py-0.25 px-1.5'
                     type='text' />
            </label>
            <p>x</p>
            <label>
              <input placeholder="P" v-model='form.depth'
                     class='w-16 text-lg border bg-gray-100 rounded-full focus:border-gray-900 border-transparent outline-none border- focus:bg-white py-0.25 px-1.5'
                     type='text' />
            </label>
            <p>{{  $t('in') }} cm</p>
          </div>
          <div class='flex flex-row justify-between items-center space-x-2'>
            <span class='icon-download3'></span>
            <label>
              <input :placeholder="$t('parcel_weight')" v-model='form.weight'
                     class='w-20 text-lg border bg-gray-100 rounded-full focus:border-gray-900 border-transparent outline-none border- focus:bg-white py-0.25 px-1.5'
                     type='text' />
            </label>
            <p>{{  $t('in') }} kg</p>
          </div>
          <label class='flex flex-row justify-between items-center space-x-2'>
            <span class='icon-spinner4'></span>
            <p>{{ $t('packaging') }}</p>
            <select v-model='form.packaging' class='w-full border bg-white rounded px-3 py-2 outline-none w-full'>
              <option class='py-1' value='carton'>{{  $t('carton') }}</option>
              <option class='py-1' value='styrofoam'>{{  $t('styrofoam') }}</option>
              <option class='py-1' value='paper'>{{  $t('paper') }}</option>
            </select>
          </label>
          <label class='flex flex-row justify-between items-center space-x-2'>
            <span class='icon-info'></span>
            <p>Type</p>
            <select v-model='form.type' class='w-full border bg-white rounded px-3 py-2 outline-none w-full'>
              <option class='py-1' value='documents'>Documents</option>
              <option class='py-1' value='goods'>{{  $t('goods') }}</option>
              <option class='py-1' value='others'>{{  $t('others') }}</option>
            </select>
          </label>
          <div class='flex flex-row justify-between items-center space-x-2'>
            <label>
              <input type='checkbox' v-model='form.assured' />
              {{ $t('assured') }}
            </label>
          </div>
          <label>
            <input v-model='form.fragile' type='checkbox' />
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
        type: '',
        fragile: false,
        assured: false,
        weight: '',
        packaging: '',
        width: '',
        height: '',
        customer: '',
        supplier:'',
      }

    }
  },
  methods: {
    register: async function(){

      let formData = new FormData();
      formData.append('type', this.form.type)
      formData.append('fragile', '' + this.form.fragile)
      formData.append('assured', '' + this.form.assured)
      formData.append('weight', this.form.weight)
      formData.append('packaging', this.form.packaging)
      formData.append('width', this.form.width)
      formData.append('height', this.form.height)
      formData.append('customer', this.form.customer)
      formData.append('supplier', this.form.supplier)
      let req = await this.$axios.post('entities/parcels/add', formData)
    }
  }
})
</script>

<style lang='scss' scoped></style>