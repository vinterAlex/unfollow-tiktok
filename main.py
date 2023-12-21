import time
import pyautogui

def is_box_red(box_position):
    # Example: Check if the box is red by checking a pixel color
    # You might need to adjust this based on the actual color of the "Following" box
    pixel_color = pyautogui.screenshot().getpixel((box_position.left, box_position.top))
    return pixel_color == (255, 0, 0)  # Example RGB value for red

def is_gray_box(box_position):
    # Example: Check if the box is gray by checking a pixel color
    # You might need to adjust this based on the actual color of the "gray" box
    pixel_color = pyautogui.screenshot().getpixel((box_position.left, box_position.top))
    return pixel_color == (169, 169, 169)  # Example RGB value for gray

def click_following_boxes():
    # Give some time for the user to position the mouse
    time.sleep(5)

    gray_box_image_path = 'following_box.png'  # Provide the path to the image of a gray box
    boxes_to_click = 6  # Number of boxes to click at once

    try:
        while True:
            # Find the "Following" boxes on the screen
            following_positions = list(pyautogui.locateAllOnScreen('following_box.png'))

            if following_positions:
                # Click on the first 'boxes_to_click' number of boxes
                for following_position in following_positions[:boxes_to_click]:
                    if is_box_red(following_position):
                        # Scroll the page with a higher scroll amount for faster scrolling
                        pyautogui.scroll(200, x=0, y=0)
                        time.sleep(0.1)  # Adjust sleep time as needed for smoother scrolling
                    else:
                        # Box is gray, click on it
                        pyautogui.click(following_position.left + following_position.width // 2,
                                        following_position.top + following_position.height // 2)
                
                # Wait for a short duration to allow the actions to complete
                time.sleep(0.5)
                
            else:
                # If the "Following" box is not found, break the loop
                break

            # Scroll up until at least 5 gray boxes appear on the screen
            pyautogui.scroll(-200, x=0, y=0)
            time.sleep(0.1)
            gray_positions = list(pyautogui.locateAllOnScreen(gray_box_image_path))
            while len(gray_positions) < 5:
                pyautogui.scroll(-200, x=0, y=0)
                time.sleep(0.1)
                gray_positions = list(pyautogui.locateAllOnScreen(gray_box_image_path))

            # Click on the gray boxes
            for gray_position in gray_positions[:5]:
                if is_gray_box(gray_position):
                    pyautogui.click(gray_position.left + gray_position.width // 2,
                                    gray_position.top + gray_position.height // 2)
                    time.sleep(0.5)

    except KeyboardInterrupt:
        print("Execution interrupted by user.")

if __name__ == "__main__":
    click_following_boxes()
