import pygame
import sys
import random

# --- Impostazioni di base ---
LARGHEZZA = 640
ALTEZZA = 480
DIM_CELLA = 20

# Calcolo delle celle in orizzontale e verticale
CELLE_X = LARGHEZZA // DIM_CELLA
CELLE_Y = ALTEZZA // DIM_CELLA

# Colori (R, G, B)
NERO = (0, 0, 0)
BIANCO = (255, 255, 255)
VERDE = (0, 200, 0)
ROSSO = (200, 0, 0)

# Velocità del gioco (frame per secondo)
FPS = 10


class Snake:
    def __init__(self):
        # Partiamo dal centro
        self.posizioni = [(CELLE_X // 2, CELLE_Y // 2)]
        # Direzione iniziale: verso destra
        self.direzione = (1, 0)
        self.crescere = False

    def cambia_direzione(self, nuova_direzione):
        """
        nuova_direzione è una tupla (dx, dy).
        Evitiamo di permettere di andare subito nella direzione opposta.
        """
        dx, dy = nuova_direzione
        odx, ody = self.direzione

        # Impedisci inversione totale (es. da destra a sinistra)
        if (dx, dy) == (-odx, -ody):
            return

        self.direzione = (dx, dy)

    def aggiorna(self):
        """
        Muove il serpente: aggiunge una nuova testa
        e rimuove la coda, salvo quando deve crescere.
        """
        head_x, head_y = self.posizioni[0]
        dx, dy = self.direzione
        nuova_testa = (head_x + dx, head_y + dy)

        # Inserisci nuova testa
        self.posizioni.insert(0, nuova_testa)

        # Se non deve crescere, togli l'ultima cella
        if not self.crescere:
            self.posizioni.pop()
        else:
            self.crescere = False

    def mangia(self):
        """Indica che il serpente deve crescere di 1 nella prossima mossa."""
        self.crescere = True

    def colpisce_pareti(self):
        """Controlla se la testa è fuori schermo."""
        head_x, head_y = self.posizioni[0]
        return not (0 <= head_x < CELLE_X and 0 <= head_y < CELLE_Y)

    def colpisce_se_stesso(self):
        """Controlla se la testa tocca una parte del corpo."""
        testa = self.posizioni[0]
        return testa in self.posizioni[1:]


class Cibo:
    def __init__(self, snake_posizioni):
        self.posizione = self.genera_posizione(snake_posizioni)

    def genera_posizione(self, snake_posizioni):
        """Genera una posizione che non sia sul serpente."""
        while True:
            x = random.randint(0, CELLE_X - 1)
            y = random.randint(0, CELLE_Y - 1)
            if (x, y) not in snake_posizioni:
                return (x, y)

    def respawn(self, snake_posizioni):
        self.posizione = self.genera_posizione(snake_posizioni)


def disegna_griglia(schermo):
    for x in range(0, LARGHEZZA, DIM_CELLA):
        pygame.draw.line(schermo, (40, 40, 40), (x, 0), (x, ALTEZZA))
    for y in range(0, ALTEZZA, DIM_CELLA):
        pygame.draw.line(schermo, (40, 40, 40), (0, y), (LARGHEZZA, y))


def disegna_snake(schermo, snake):
    for (x, y) in snake.posizioni:
        rect = pygame.Rect(x * DIM_CELLA, y * DIM_CELLA, DIM_CELLA, DIM_CELLA)
        pygame.draw.rect(schermo, VERDE, rect)


def disegna_cibo(schermo, cibo):
    x, y = cibo.posizione
    rect = pygame.Rect(x * DIM_CELLA, y * DIM_CELLA, DIM_CELLA, DIM_CELLA)
    pygame.draw.rect(schermo, ROSSO, rect)


def mostra_punteggio(schermo, font, punteggio):
    testo = font.render(f"Score: {punteggio}", True, BIANCO)
    schermo.blit(testo, (10, 10))


def mostra_game_over(schermo, font, punteggio):
    testo1 = font.render("GAME OVER", True, ROSSO)
    testo2 = font.render(f"Score: {punteggio}", True, BIANCO)
    testo3 = font.render("Press SPACE to play again o ESC to exit", True, BIANCO)

    rect1 = testo1.get_rect(center=(LARGHEZZA // 2, ALTEZZA // 2 - 30))
    rect2 = testo2.get_rect(center=(LARGHEZZA // 2, ALTEZZA // 2))
    rect3 = testo3.get_rect(center=(LARGHEZZA // 2, ALTEZZA // 2 + 30))

    schermo.blit(testo1, rect1)
    schermo.blit(testo2, rect2)
    schermo.blit(testo3, rect3)


def main():
    pygame.init()
    schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
    pygame.display.set_caption("Snake con pygame")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    # Stato iniziale del gioco
    snake = Snake()
    cibo = Cibo(snake.posizioni)
    punteggio = 0
    game_over = False

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                # Controlli del serpente
                if not game_over:
                    if event.key == pygame.K_UP:
                        snake.cambia_direzione((0, -1))
                    elif event.key == pygame.K_DOWN:
                        snake.cambia_direzione((0, 1))
                    elif event.key == pygame.K_LEFT:
                        snake.cambia_direzione((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        snake.cambia_direzione((1, 0))
                else:
                    # Dopo il game over: spazio per ricominciare
                    if event.key == pygame.K_SPACE:
                        snake = Snake()
                        cibo = Cibo(snake.posizioni)
                        punteggio = 0
                        game_over = False

        if not game_over:
            # Aggiorna logica di gioco
            snake.aggiorna()

            # Controlla collisione con cibo
            if snake.posizioni[0] == cibo.posizione:
                snake.mangia()
                punteggio += 1
                cibo.respawn(snake.posizioni)

            # Controlla collisioni letali
            if snake.colpisce_pareti() or snake.colpisce_se_stesso():
                game_over = True

        # Disegno
        schermo.fill(NERO)
        disegna_griglia(schermo)
        disegna_snake(schermo, snake)
        disegna_cibo(schermo, cibo)
        mostra_punteggio(schermo, font, punteggio)

        if game_over:
            mostra_game_over(schermo, font, punteggio)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()