<script setup lang="ts">
import { useConfirm } from "primevue/useconfirm";
import ConfirmDialog from 'primevue/confirmdialog';
const confirm = useConfirm();
const confirmPosition = (position: string) => {
    confirm.require({
        group: 'positioned',
        message: 'Are you sure you want to continue?',
        icon: 'pi pi-exclamation-triangle',
        accept: () => {
            alert(`Position: ${position}`);
        },
        reject: () => {
            alert(`Position: ${position}`);
        },
    });
}

</script>

<template>
    <div class="container flex items-center about bg-slate-200">
        <ConfirmDialog group="positioned"></ConfirmDialog>
        <div class="flex flex-wrap justify-center gap-2 mb-4">
            <Button @click="confirmPosition('topleft')" icon="pi pi-arrow-down-right" label="TopLeft"
                severity="secondary" style="min-width: 10rem">3</Button>
            <Button @click="confirmPosition('top')" icon="pi pi-arrow-down" label="Top" severity="secondary"
                style="min-width: 10rem">2</Button>
            <Button @click="confirmPosition('topright')" icon="pi pi-arrow-down-left" label="TopRight"
                severity="secondary" style="min-width: 10rem">1</Button>
        </div>
    </div>
</template>

<style></style>