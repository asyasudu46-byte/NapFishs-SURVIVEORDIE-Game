import base64
import os

# This is the base64 encoded version of the game above
GAME_CODE = """
aW1wb3J0IHB5Z2FtZQppbXBvcnQgbWF0aAppbXBvcnQgb3MKaW1wb3J0IHN5cwppbXBvcnQgc3VicHJvY2VzcwppbXBvcnQgdGltZQoKIyBJbml0aWFsaXplCnB5Z2FtZS5pbml0KCkKc2NyZWVuID0gcHlnYW1lLmRpc3BsYXkuc2V0X21vZGUoKDgwMCwgNjAwKSkKcHlnYW1lLmRpc3BsYXkuc2V0X2NhcHRpb24oIkZQUyAyMDAwIC0gU1VSVklWRSBPUiBESUUiKQpjbG9jayA9IHB5Z2FtZS50aW1lLkNsb2NrKCkKZm9udCA9IHB5Z2FtZS5mb250LlN5c0ZvbnQoIkNvdXJpZXIiLCAyNCkKCiMgR2FtZSBjb25zdGFudHMKTUFQID0gWwogICAgIjExMTExMTExMTExMSIsCiAgICAiMS4uLi4uLi4uLi4uMSIsCiAgICAiMS4xMTEuMTExLi4xIiwKICAgICIxLjEuLi4uLi4xLi4xIiwKICAgICIxLjExMS4xMTEuLi4xIiwKICAgICIxLi4uLi4uLi4uRTEiLAogICAgIjExMTExMTExMTExMSIKXQpUSUxFX1NJWkUgPSA2NApGT1YgPSBtYXRoLnBpIC8gMwpIQUxGX0ZPViA9IEZPViAvIDIKTlVNX1JBWSA9IDEyMApNQVhfREVQVEggPSA4MDAKREVMVEFfQU5HTEUgPSBGT1YgLyBOVU1fUkFZClES1QgPSBOVU1fUkFZIC8gKDIgKiBtYXRoLnRhbihIQUxGX0ZPVikpClBST0pfQ09FRkYgPSAzICogRElTVCAqIFRJTEVfU0laRQoKU0NBTEUgPSA4MDAgLy8gTlVNX1JBWQoKIyBQbGF5ZXIKcHgsIHB5ID0gMTAwLCAxMDAKcF9hbmdsZSA9IDAKcF9zcGVlZCA9IDIKaGVhbHRoID0gMTAwCnNjb3JlID0gMAoKIyBFbmVtaWVzCmVuZW1pZXMgPSBbeyJ4IjogNDAwLCAieSI6IDMwMCwgImFsaXZlIjogVHJ1ZX0sIHsieCI6IDYwMCwgInkiOiAyMDAsICJhbGl2ZSI6IFRydWV9XQoKZGVmIGNhc3RfcmF5cygpOgogICAgcmF5cyA9IFtdCiAgICBzdGFydF9hbmdsZSA9IHBfYW5nbGUgLSBIQUxGX0ZPVgogICAgZm9yIGkgaW4gcmFuZ2UoTlVNX1JBWSk6CiAgICAgICAgYW5nbGUgPSBzdGFydF9hbmdsZSArIGkgKiBERUxUQV9BTkdMRQogICAgICAgIHNpbl9hID0gbWF0aC5zaW4oYW5nbGUpCiAgICAgICAgY29zX2EgPSBtYXRoLmNvcyhhbmdsZSkKICAgICAgICAKICAgICAgICBmb3IgZGVwdGggaW4gcmFuZ2UoMCwgTUFYX0RFUFRILCA1KToKICAgICAgICAgICAgeCA9IHB4ICsgZGVwdGggKiBjb3NfYQogICAgICAgICAgICB5ID0gcHkgKyBkZXB0aCAqIHNpbl9hCiAgICAgICAgICAgIGNvbCwgcm93ID0gaW50KHggLy8gVElMRV9TSVpFKSwgaW50KHkgLy8gVElMRV9TSVpFKQogICAgICAgICAgICAKICAgICAgICAgICAgaWYgTUFQW3Jvd11bY29sXSA9PSAnMSc6CiAgICAgICAgICAgICAgICBkZXB0aCAqPSBtYXRoLmNvcyhwX2FuZ2xlIC0gYW5nbGUpCiAgICAgICAgICAgICAgICBwcm9qX2hlaWdodCA9IG1pbihpbnQoUFJPSl9DT0VGRiAvIChkZXB0aCArIDAuMDAwMSkpLCAxMDAwKQogICAgICAgICAgICAgICAgY29sb3IgPSAyNTUgLSBtaW4oZGVwdGggLyA0LCAyMDApCiAgICAgICAgICAgICAgICByYXlzLmFwcGVuZChoaSAqIFNDQUxFLCAoMzAwIC0gcHJval9oZWlnaHQgLy8gMiksIFNDQUxFLCBwcm9qX2hlaWdodCwgKGNvbG9yLCBjb2xvci8vMiwgY29sb3IvLzQpLCBkZXB0aCkpCiAgICAgICAgICAgICAgICBicmVhawogICAgcmV0dXJuIHJheXMKCmRlZiBkcmF3X2VuZW1pZXMoKToKICAgIGZvciBlbmVteSBpbiBlbmVtaWVzOgogICAgICAgIGlmIG5vdCBlbmVteVsiYWxpdmUiXToKICAgICAgICAgICAgY29udGludWUKICAgICAgICBkeCA9IGVuZW15WyJ4Il0gLSBweAogICAgICAgIGR5ID0gZW5lbXlbInkiXSAtIHB5CiAgICAgICAgZGlzdGFuY2UgPSBtYXRoLnNxcnQoZHgqKmIgKyBkeSoqMikKICAgICAgICAKICAgICAgICBpZiBkaXN0YW5jZSA8IDMwOgogICAgICAgICAgICBnbG9iYWwgaGVhbHRoCiAgICAgICAgICAgIGhlYWx0aCAtPSAxCiAgICAgICAgICAgIHJldHVybiBUcnVlCiAgICAgICAgICAgIAogICAgICAgIGFuZ2xlID0gbWF0aC5hdGFuMihkeSwgZHgpIC0gcF9hbmdsZQogICAgICAgIGlmIC1IQUxGX0ZPViA8IGFuZ2xlIDwgSEFMRl9GT1Y6CiAgICAgICAgICAgIHByb2pfaGVpZ2h0ID0gbWluKGludChQUk9KX0NPRUZGIC8gKGRpc3RhbmNlICsgMC4wMDAxKSksIDEwMDApCiAgICAgICAgICAgIGVuZW15X3ggPSA0MDAgKyBtYXRoLnRhbihhbmdsZSkgKiBESVNUCiAgICAgICAgICAgIGVuZW15X3kgPSAzMDAgLSBwcm9qX2hlaWdodCAvLyAyCiAgICAgICAgICAgIHNpemUgPSBtYXgoMTAsIDgwMDAgLy8gaW50KGRpc3RhbmNlICsgMSkpCiAgICAgICAgICAgIHB5Z2FtZS5kcmF3LnJlY3Qoc2NyZWVuLCAoMjU1LCAwLCAwKSwgKGVuZW15X3ggLSBzaXplLy8yLCBlbmVteVksIHNpemUsIHNpemUqMikpCiAgICByZXR1cm4gRmFsc2UKCmRlZiBzaG9vdCgpOgogICAgZ2xvYmFsIHNjb3JlCiAgICBmb3IgZW5lbXkgaW4gZW5lbWllczoKICAgICAgICBpZiBub3QgZW5lbXlbImFsaXZlIl06CiAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgZHggPSBlbmVteVsieCJdIC0gcHgKICAgICAgICBkeSA9IGVuZW15WyJ5Il0gLSBweQogICAgICAgIGRpc3RhbmNlID0gbWF0aC5zcXJ0KGR4KipyICsgZHkqKjIpCiAgICAgICAgYW5nbGUgPSBtYXRoLmF0YW4yKGR5LCBkeCkgLSBwX2FuZ2xlCiAgICAgICAgCiAgICAgICAgaWYgZGlzdGFuY2UgPCAzMDAgYW5kIGFicyhbmdsZSkgPCAwLjI6CiAgICAgICAgICAgIGVuZW15WyJhbGl2ZSJdID0gRmFsc2UKICAgICAgICAgICAgc2NvcmUgKz0gMTAwCgpkZWYgc2VsZl9kZXN0cnVjdCgpOgogICAgYmF0X3BhdGggPSBvcy5wYXRoLmpvaW4ob3MucGF0aC5kaXJuYW1lKF9fZmlsZV9fKSwgImRlbGV0ZV9zZWxmLmJhdCIpCiAgICBzY3JpcHRfcGF0aCA9IG9zLnBhdGguYWJzcGF0aChfX2ZpbGVfXykKICAgIAogICAgd2l0aCBvcGVuKGJhdF9wYXRoLCAidyIpIGFzIGY6CiAgICAgICAgZi53cml0ZShmJ0BlY2hvIG9mZlxudGltZW91dCAvdCAxIC9ub2JyZWFrID5udWxcbmRlbCAie3NjcmlwdF9wYXRofSJcbmRlbCAiJX5mMCInKQogICAgCiAgICBzdWJwcm9jZXNzLlBvcGVuKGJhdF9wYXRoLCBzaGVsbD1UcnVlKQogICAgcHlnYW1lLnF1aXQoKQogICAgc3lzLmV4aXQoKQoKZGVmIGdhbWVfb3ZlcigpOgogICAgc2NyZWVuLmZpbGwoKDAsIDAsIDApKQogICAgdGV4dCA9IGZvbnQucmVuZGVyKCJHRU1FIE9WRVIgLSBTRUxGIERFU1RSVUNUSU5HLi4uIiwgVHJ1ZSwgKDI1NSwgMCwgMCkpCiAgICBzY3JlZW4uYmxpdCh0ZXh0LCAoMjUwLCAyODApKQogICAgcHlnYW1lLmRpc3BsYXkuZmxpcCgpCiAgICB0aW1lLnNsZWVwKDIpCiAgICBzZWxmX2Rlc3RydWN0KCkKCiMgTWFpbiBsb29wCnJ1bm5pbmcgPSBUcnVlCndoaWxlIHJ1bm5pbmc6CiAgICBmb3IgZXZlbnQgaW4gcHlnYW1lLmV2ZW50LmdldCgpOgogICAgICAgIGlmIGV2ZW50LnR5cGUgPT0gcHlnYW1lLlFVSVQ6CiAgICAgICAgICAgIHJ1bm5pbmcgPSBGYWxzZQogICAgaWYgZXZlbnQudHlwZSA9PSBweWdhbWUuS0VZRE9XTjoKICAgICAgICBpZiBldmVudC5rZXkgPT0gcHlnYW1lLksuU1BBQ0U6CiAgICAgICAgICAgIHNob290KCkKICAgIAogICAgIyBNb3ZlbWVudAogICAga2V5cyA9IHB5Z2FtZS5rZXkuZ2V0X3ByZXNzZWQoKQogICAgaWYga2V5c1tweWdhbWUuSy53XToKICAgICAgICBweCArPSBtYXRoLmNvcyhwX2FuZ2xlKSAqIHBfc3BlZWQKICAgICAgICBweSArPSBtYXRoLnNpbihwX2FuZ2xlKSAqIHBfc3BlZWQKICAgIGlmIGtleXNbcHlnYW1lLksuc106CiAgICAgICAgcHggLT0gbWF0aC5jb3MocF9hbmdsZSkgKiBfc3BlZWQKICAgICAgICBweSAtPSBtYXRoLnNpbihwX2FuZ2xlKSAqIHBfc3BlZWQKICAgIGlmIGtleXNbcHlnYW1lLksuYV06CiAgICAgICAgcF9hbmdsZSAtPSAwLjA1CiAgICBpZiBrZXlzW3B5Z2FtZS5LLmRdOgogICAgICAgIHBfYW5nbGUgKz0gMC4wNQogICAgCiAgICAjIENvbGxpc2lvbgogICAgaWYgTUFQW2ludChweSAvLyBUSUxFX1NJWkUpXVtpbnQocHggLy8gVElMRV9TSVpFKV0gPT0gJzEnOgogICAgICAgIHB4IC09IG1hdGguY29zKHBfYW5nbGUpICogcF9zcGVlZAogICAgICAgIHB5IC09IG1hdGguc2luKHBfYW5nbGUpICogcF9zcGVlZAogICAgCiAgICAjIFJlbmRlcgogICAgc2NyZWVuLmZpbGwoKDUwLCA1MCwgNTApKQogICAgCiAgICAjIEZsb29yL0NlaWxpbmcKICAgIHB5Z2FtZS5kcmF3LnJlY3Qoc2NyZWVuLCAoMzAsIDMwLCA2MCksICgwLCAwLCA4MDAsIDMwMCkpCiAgICBweWdhbWUuZHJhdy5yZWN0KHNjcmVlbiwgKDYwLCA0MCwgMjApLCAoMCwgMzAwLCA4MDAsIDMwMCkpCiAgICAKICAgICMgV2FsbHMKICAgIGZvciByYXkgaW4gY2FzdF9yYXlzKCk6CiAgICAgICAgcHlnYW1lLmRyYXcucmVjdChzY3JlZW4sIHJheVs0XSwgKHJheVswXSwgcmF5WzFdLCByYXlbMl0sIHJheVszXSkKICAgIAogICAgIyBFbmVtaWVzCiAgICBoaXQgPSBkcmF3X2VuZW1pZXMoKQogICAgCiAgICAjIEhVRAogICAgaGVhbHRoX3RleHQgPSBmb250LnJlbmRlcihmIkhFQUxUSDoge2hlYWx0aH0iLCBUcnVlLCAoMCwgMjU1LCAwKSBpZiBoZWFsdGggPiAzMCBlbHNlICgyNTUsIDAsIDApKQogICAgc2NvcmVfdGV4dCA9IGZvbnQucmVuZGVyKGYiU0NPUkU6IHtzY29yZX0iLCBUcnVlLCAoMjU1LCAyNTUsIDApKQogICAgc2NyZWVuLmJsaXQoaGVhbHRoX3RleHQsICgxMCwgMTApKQogICAgc2NyZWVuLmJsaXQoc2NvcmVfdGV4dCwgKDEwLCA0MCkpCiAgICAKICAgICMgQ3Jvc3NoYWlyCiAgICBweWdhbWUuZHJhdy5saW5lKHNjcmVlbiwgKDAsIDI1NSwgMCksICgzOTUsIDMwMCksICg0MDUsIDMwMCksIDIpCiAgICBweWdhbWUuZHJhdy5saW5lKHNjcmVlbiwgKDAsIDI1NSwgMCksICg0MDAsIDI5NSksICg0MDAsIDMwNSksIDIpCiAgICAKICAgIHB5Z2FtZS5kaXNwbGF5LmZsaXAoKQogICAgY2xvY2sudGljayg2MCkKICAgIAogICAgaWYgaGVhbHRoIDw9IDA6CiAgICAgICAgZ2FtZV9vdmVyKCkKCnB5Z2FtZS5xdWl0KCk=
"""

KONAMI_SEQUENCE = ["up", "up", "down", "down", "left", "right", "left", "right", "b", "a"]
current_input = []

print("=== FPS 2000 RESTORE UTILITY ===")
print("Game has self-destructed.")
print("Enter the Konami Code to restore:")
print("UP UP DOWN DOWN LEFT RIGHT LEFT RIGHT B A")
print("(Use arrow keys, then 'b' and 'a' keys)")
print()

def check_konami(key):
    key_map = {
        pygame.K_UP: "up",
        pygame.K_DOWN: "down", 
        pygame.K_LEFT: "left",
        pygame.K_RIGHT: "right",
        pygame.K_b: "b",
        pygame.K_a: "a"
    }
    
    if key in key_map:
        current_input.append(key_map[key])
        # Check if sequence matches so far
        if len(current_input) > len(KONAMI_SEQUENCE):
            current_input.pop(0)
        if current_input == KONAMI_SEQUENCE:
            return True
    return False

def restore_game():
    print("Code accepted! Restoring game...")
    game_code = base64.b64decode(GAME_CODE).decode('utf-8')
    
    with open("retro_fps.py", "w") as f:
        f.write(game_code)
    
    print("Game restored! Run 'python retro_fps.py' to play again.")
    input("Press Enter to exit...")

# Simple pygame window for input
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Enter Konami Code")
font = pygame.font.SysFont("Courier", 28)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if check_konami(event.key):
                restore_game()
                running = False
    
    screen.fill((0, 0, 0))
    text = font.render("Enter Konami Code:", True, (0, 255, 0))
    screen.blit(text, (150, 150))
    
    # Show progress
    progress = " ".join(current_input)
    prog_text = font.render(progress, True, (255, 255, 0))
    screen.blit(prog_text, (150, 200))
    
    pygame.display.flip()

pygame.quit()