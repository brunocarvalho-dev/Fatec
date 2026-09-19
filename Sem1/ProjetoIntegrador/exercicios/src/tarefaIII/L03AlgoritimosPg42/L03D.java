package tarefaIII.L03AlgoritimosPg42;

import javax.swing.*;

/*
d. Ler quatro valores referentes a quatro notas escolares de um aluno e imprimir uma mensagem
dizendo que o aluno foi aprovado, se o valor da média escolar for maior ou igual a 7. Se o valor da
média for menor que 7, solicitar a nota de exame, somar com o valor da média e obter nova média.
Se a nova média for maior ou igual a 5, apresentar uma mensagem dizendo que o aluno foi
aprovado em exame. Se o aluno não foi aprovado, indicar uma mensagem informando esta
condição. Apresentar com as mensagens o valor da média do aluno, para qualquer condição.
 */
public class L03D {
    static void main() {

        Float[] nota1 = new Float[5];
        float media = Float.MIN_VALUE;

        for (int i = 0; i < nota1.length; ) {
            nota1[i] = lerNota("Digite a nota " + (i + 1) + " do aluno (entre 0 e 10): ");
            i++;
            if (i == 4) {
                media = (nota1[0] + nota1[1] + nota1[2] + nota1[3]) / 4;
                if (media < 7) {
                    JOptionPane.showMessageDialog(null, "Sua média foi " + String.format("%.1f", media) + ","
                            + "\nvocê não atingiu o mínimo de 7 pontos, portanto, será necessário realizar o exame.");
                    nota1[4] = lerNota("Digite a nota do exame (entre 0 e 10): ");
                    media = (nota1[0] + nota1[1] + nota1[2] + nota1[3] + nota1[4]) / 5;

                }
            }
        }
        JOptionPane.showMessageDialog(null, aprovacao(media));
    }

    public static float lerNota(String mensagem) {
        boolean valid = true;
        float nota = -1;
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
