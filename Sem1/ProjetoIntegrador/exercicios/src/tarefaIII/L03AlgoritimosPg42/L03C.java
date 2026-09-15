package tarefaIII.L03AlgoritimosPg42;

/*c. Ler quatro valores referentes a quatro notas escolares de um aluno e imprimir uma mensagem
dizendo que o aluno foi aprovado, se o valor da média escolar for maior ou igual a 5. Se o aluno não
foi aprovado, indicar uma mensagem informando esta condição. Apresentar junto das mensagens o
valor da média do aluno para qualquer condição.
 */

public class L03C {
    static void main(String[] args) {
        Float[] nota1 = new Float[4];

        for (int i = 0; i < nota1.length; ) {
            nota1[i] = lerNota("Digite a nota " + (i + 1) + " do aluno (entre 0 e 10): ");
            i++;
        }
        float media = (nota1[0] + nota1[1] + nota1[2] + nota1[3]) / 4;

        System.out.print(aprovacao(media));
    }

    private static float lerNota(String mensagem) {
        boolean valid = true;
        float nota = Float.MIN_VALUE;
        while (valid) {
            try {
                nota = Float.valueOf(javax.swing.JOptionPane.showInputDialog(mensagem).replace(",", "."));
                if (nota < 0 || nota > 10) {
                    javax.swing.JOptionPane.showMessageDialog(null, "Nota inválida. Por favor, digite um valor entre 0 e 10.");
                } else {
                    valid = false;
                }
            } catch (NumberFormatException e) {
                javax.swing.JOptionPane.showMessageDialog(null, "Entrada inválida. Por favor, digite um número.");
            }
        }
        return nota;
    }

    private static String aprovacao(float media) {
        String msg = "";
        if (media < 5) {
            msg = ("\nAluno(a) reprovado!!\nSua nota foi" + String.format("%.1f", media) + " não atingiu o minino de 5 pontos! :(\n");
        } else if (media < 9) {
            msg = ("\nAluno(a) aprovado!!\nSua nota foi " + String.format("%.1f", media) + ", atingiu o minino de 5 pontos.\n");
        } else {
            msg = ("\nAluno(a) Aprovado!!\nSua nota foi " + String.format("%.1f", media) + ", parabéns pelo seu desempenho!! :)\n");
        }
        return msg;
    }
}
