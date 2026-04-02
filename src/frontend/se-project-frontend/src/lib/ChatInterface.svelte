<script lang="js">
     import { injectAuthToken } from './global_state/Token.svelte';
     import { getFastAPI } from './api/gen/fastAPI';
     import { global_username } from './global_state/Username.svelte';

     const api = getFastAPI(injectAuthToken())

     let title = $state('')
     let input = $state('')

     let message_list = $state([])

     async function onSubmit(event) {
          event.preventDefault()
          message_list.push({
               "role": "user",
               "content": input,
          })
          input = ''

          try {
               console.log({ 
                    "username": global_username,
                    "title": title,
                    "content": JSON.stringify(message_list)
               })
               const res = await api.directGenerationGeneratePost({ 
                    "username": global_username.value,
                    "title": title,
                    "content": JSON.stringify(message_list)
               });
               let res_content = res.data["content"]
               let res_title = res.data["title"]
               if (typeof res_content === "string") {
                    message_list.push({
                         "role": "assistant",
                         "content": res_content
                    })
               }
               if (typeof res_title === "string") {
                    title = res_title
               }

          } catch (error) {
               console.error("Failed to get model response")
          }
     }

</script>

<main class="h-full bg-black text-white flex flex-col">
     <header class="border-b border-gray-800 px-6 py-4 flex-shrink-0">
          <h1 class="text-xl font-semibold">{title ? title: "New Chat"}</h1>
     </header>
     <div class="flex-1 overflow-y-auto p-6 space-y-6">
          {#each message_list as message}
               <div class="flex {message.role === 'user' ? 'justify-end' : 'justify-start'}">
                    <div class="max-w-2xl {message.role === 'user' ? 'bg-gray-800' : 'bg-gray-900'} rounded-2xl px-5 py-3 {message.role === 'user' ? 'rounded-br-md' : 'rounded-bl-md'}">
                         <p class="whitespace-pre-wrap">{message.content}</p>
                    </div>
               </div>
          {/each}
     </div>
     <footer class="border-t border-gray-800 p-4 flex-shrink-0">
          <form class="max-w-3xl mx-auto flex gap-3" onsubmit={onSubmit}>
               <input class="flex-1 px-4 py-3 bg-gray-900 border border-gray-700 rounded-full text-white placeholder-gray-500 focus:outline-none focus:border-gray-500" type="text" placeholder="Message..." bind:value={input}/>
               <button type="submit" class="px-6 py-3 bg-gray-700 hover:bg-gray-600 rounded-full font-medium transition">Send</button>
          </form>
     </footer>
</main>
