<script>
    import {createEventDispatcher} from 'svelte';
    const dispatch = createEventDispatcher();

    export let active = false
    export let title
    export let tabId
    export let iconClass

   $: navItemClass = active ? "nav-item active" : "nav-item";
    let changeTab = () => {
        if (active) {
            dispatch("navClick", {
                refreshTab: true
            })
        } else {
            // navItemClass = "nav-item active"
            active = true
            dispatch("navClick", {
                changeTab: tabId
            })
        }
    }
</script>

<li class={navItemClass}>
    <a class="nav-link" href="javascript:;" on:click={()=> changeTab()}>
        <i class={iconClass}></i>
        <span>{title}</span>
    </a>
</li>