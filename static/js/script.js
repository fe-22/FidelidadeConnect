document.addEventListener("DOMContentLoaded", function() {
    const addChildButton = document.getElementById('adicionar_filho');
    const form = document.getElementById('cadastroForm');

    // Adicionar novo campo para filhos
    addChildButton.addEventListener('click', function() {
        const fieldset = document.createElement('fieldset');
        fieldset.classList.add('adicionar_filho');

        const filhoLabel = document.createElement('label');
        filhoLabel.setAttribute('for', 'filho');
        filhoLabel.textContent = 'Nome do Filho:';
        fieldset.appendChild(filhoLabel);

        const filhoInput = document.createElement('input');
        filhoInput.setAttribute('type', 'text');
        filhoInput.setAttribute('id', 'filho');
        filhoInput.setAttribute('name', 'filho[]');
        filhoInput.setAttribute('placeholder', 'Nome do Filho');
        filhoInput.required = true;
        fieldset.appendChild(filhoInput);

        const br = document.createElement('br');
        fieldset.appendChild(br);

        const dataNascimentoLabel = document.createElement('label');
        dataNascimentoLabel.setAttribute('for', 'data_nascimento_filho');
        dataNascimentoLabel.textContent = 'Data de Nascimento:';
        fieldset.appendChild(dataNascimentoLabel);

        const dataNascimentoInput = document.createElement('input');
        dataNascimentoInput.setAttribute('type', 'date');
        dataNascimentoInput.setAttribute('id', 'data_nascimento_filho');
        dataNascimentoInput.setAttribute('name', 'data_nascimento_filho[]');
        dataNascimentoInput.setAttribute('placeholder', 'Data de Nascimento');
        dataNascimentoInput.required = true;
        fieldset.appendChild(dataNascimentoInput);

        addChildButton.parentNode.insertBefore(fieldset, addChildButton);
    });

    // Validação básica do formulário antes do envio
    form.addEventListener('submit', function(event) {
        const nome = document.getElementById('nome').value;
        const email = document.getElementById('email').value;
        const telefoneFixo = document.getElementById('telefone_fixo').value;
        const telefoneCelular = document.getElementById('telefone_celular').value;
        const redesSociais = document.getElementById('redes_sociais').value;

        if (!nome || !email || !telefoneFixo || !telefoneCelular || !redesSociais) {
            alert('Por favor, preencha todos os campos obrigatórios.');
            event.preventDefault();
        }
    });
});
form.addEventListener('submit', function(event) {
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const telefoneFixo = document.getElementById('telefone_fixo').value;
    const telefoneCelular = document.getElementById('telefone_celular').value;
    const redesSociais = document.getElementById('redes_sociais').value;
    

    if (!nome || !email || !telefoneFixo || !telefoneCelular || !redesSociais) {
        alert('Por favor, preencha todos os campos obrigatórios.');
        event.preventDefault();
    } else {
        // Redirecionar para a página de resultado após a validação bem-sucedida
        window.location.href = '/result';
    }
});

