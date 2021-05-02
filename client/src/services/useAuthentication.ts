import { reactive, useContext } from '@nuxtjs/composition-api'
import { success, error } from '@/services/useToast'

export function useLogin() {
  const { $auth } = useContext()
  const { $toast } = useContext()
  const state = reactive({
    email: '',
    password: ''
  })

  async function handleSubmit() {
    const { data } = (await $auth.loginWith('local', { data: state })) as any
    if (data.code == 200) {
      $toast.success(`Welcome 👋`)
    } else if (data.code == 401) {
      $toast.error(`Invalid credentials`)
    } else if (data.code == 404) {
      $toast.error(`User not found`)
    }
  }

  return {
    state,
    handleSubmit
  }
}

export function useLogout() {
  const { $auth } = useContext()

  async function handleLogout() {
    try {
      $auth.logout()
      success('You are now logged out 👋')
    } catch (error: any) {
      console.log(error)
    }
  }

  return {
    handleLogout
  }
}
