const botao = document.querySelector('#botao-copiar-link')
const anchor = document.querySelector('#anchor-copiar-link')
const container = document.querySelector('#toast-container')

function criar_toast(mensagem, background) {
    const toastEl = document.createElement("div");


    toastEl.classList.add(
        "toast",
        "align-items-center",
        "border-0",
        "mb-2",
        `bg-${background}`,
        "position-fixed",
        "bottom-0", 
        "end-0",
        "m-3"
    )
    toastEl.style = 'z-index: 1080;'
    

    toastEl.setAttribute("role", "alert");
    toastEl.setAttribute("aria-live", "assertive");
    toastEl.setAttribute("aria-atomic", "true");

    toastEl.innerHTML = `
      <div class="d-flex text-light">
        <div class="toast-body">
          ${mensagem}
        </div>
        <button type="button" class="btn-close btn-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Fechar"></button>
      </div>
    `;

    container.appendChild(toastEl)

    const toast = new bootstrap.Toast(toastEl, { delay: 3000 });

    toastEl.addEventListener("hidden.bs.toast", () => {
      toastEl.remove();
    });
    toast.show();
}

function copiar_url() {
    try {
        navigator.clipboard.writeText(window.location.href)
        criar_toast('URL copiada para a área de transferência.', 'success')
    } catch {
        criar_toast('Não foi possível copiar o link para a área de transferência.', 'danger')
    }
}

document.addEventListener('DOMContentLoaded', () => {
    botao.addEventListener('click', copiar_url)
    anchor.addEventListener('click', copiar_url)
});