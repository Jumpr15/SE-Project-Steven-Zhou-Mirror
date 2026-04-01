<script lang="js">
	import { PlusIcon, SettingsIcon, TrashIcon } from '@lucide/svelte';
	import ChatInterface from './ChatInterface.svelte';

	const chats = [
		{ id: 1, title: 'New Chat' },
	];
</script>

<div class="flex h-screen bg-black text-white">
	<aside class="w-64 border-r border-gray-800 flex flex-col bg-gray-950">
		<div class="p-3 border-b border-gray-800">
			<button class="w-full flex items-center gap-3 px-4 py-2.5 bg-gray-800 hover:bg-gray-700 rounded-lg transition font-medium">
				<PlusIcon class="size-5" />
				New Chat
			</button>
		</div>
		<div class="flex-1 overflow-y-auto p-3 space-y-1">
			{#each chats as chat}
				<button class="w-full flex items-center gap-3 px-4 py-2 text-gray-300 hover:bg-gray-800 rounded-lg transition text-left">
					<TrashIcon class="size-4 opacity-50" />
					{chat.title}
				</button>
			{/each}
		</div>
		<div class="p-3 border-t border-gray-800">
			<button class="w-full flex items-center gap-3 px-4 py-2 text-gray-400 hover:bg-gray-800 rounded-lg transition">
				<SettingsIcon class="size-5" />
				Settings
			</button>
		</div>
	</aside>
	<main class="flex-1">
		<ChatInterface />
	</main>
</div>
