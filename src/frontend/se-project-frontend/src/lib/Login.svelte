<script>
     import { push } from 'svelte-spa-router';
     import { getFastAPI } from "./api/gen/fastAPI";
     import { token } from './global_state/Token.svelte';
     import { global_username } from './global_state/Username.svelte';

     const api = getFastAPI()

     let username = $state('');
     let password = $state('');
     let error_val = $state('');

     async function onSubmit(event) {
          event.preventDefault()

          try {
               const res = await api.userLoginLoginPost({ 
                    "username": username,
                    "password": password
               })
               token.value = res.data["access_token"]
               global_username.value = username
               push('/chat')

          } catch (error) {
               console.error("Failed to login")
               error_val = "Failed to login"
          } finally {
               username = ''
               password = ''
          }
     }
</script>

<div class="min-h-screen bg-black text-white flex flex-col items-center justify-center">
     <div class="w-full max-w-md px-6">
          <div class="text-center mb-10">
               <h1 class="text-4xl font-bold mb-2">RAG Chat</h1>
               <p class="text-gray-400">Sign in to continue</p>
          </div>
          <form class="space-y-4" onsubmit={onSubmit}>
               <div>
                    <input class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:outline-none focus:border-gray-500 transition" type="text" placeholder="Username" bind:value={username}/>
               </div>
               <div>
                    <input class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:outline-none focus:border-gray-500 transition" type="password" placeholder="Password" bind:value={password}/>
               </div>
               {#if error_val}
                    <p class="text-red-400 text-sm text-center">{error_val}</p>
               {/if}
               <button type="submit" class="w-full py-3 bg-white text-black font-semibold rounded-lg hover:bg-gray-100 transition">Sign In</button>
          </form>
     </div>
</div>
