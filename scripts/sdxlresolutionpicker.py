import modules.scripts as scripts
import gradio as gr

class SDXLResolutionPicker(scripts.Script):
    
        def title(self):
                return "SDXL Resolution Picker"

        def show(self, is_img2img):
                return scripts.AlwaysVisible
        
        def ui(self, is_img2img):
            
            with gr.Accordion("SDXL Resolution Picker", open=False):

                with gr.Row():
                    
                    with gr.Column(min_width=33):
                            text1 = gr.Markdown (
                                    value="Square",
                            )
                            button0 = gr.Button (
                                    value="1024x1024",
                                    size="6sm"
                                    
                            )

                    with gr.Column(min_width=33):
                            text2 = gr.Markdown(
                                    value="Landscape",
                            )
                            button1 = gr.Button (
                                    value="1152x896",
                                    size="6sm"
                            )
                            button2 = gr.Button (
                                    value="1216x832",
                                    size="6sm"
                            )
                            button3 = gr.Button (
                                    value="1344x768",
                                    size="6sm"
                            )
                            button4 = gr.Button (
                                    value="1536x640",
                                    size="6sm"
                            )

                    with gr.Column(min_width=33):
                            text3 = gr.Markdown(
                                    value="Portrait",
                                    size="6sm"
                            )
                            button5 = gr.Button (
                                    value="896x1152",
                                    size="6sm"
                            )
                            button6 = gr.Button (
                                    value="832x1216",
                                    size="6sm"
                            )
                            button7 = gr.Button (
                                    value="768x1344",
                                    size="6sm"
                            )
                            button8 = gr.Button (
                                    value="640x1536",
                                    size="6sm"
                            )

                            button0.click(fn=None, _js="function(){setsdxlres(1024, 1024)}", inputs=None, outputs=None, show_progress=False)
                                
                            button1.click(fn=None, _js="function(){setsdxlres(1152, 896)}", inputs=None, outputs=None, show_progress=False)
                            button2.click(fn=None, _js="function(){setsdxlres(1216, 832)}", inputs=None, outputs=None, show_progress=False)
                            button3.click(fn=None, _js="function(){setsdxlres(1344, 768)}", inputs=None, outputs=None, show_progress=False)
                            button4.click(fn=None, _js="function(){setsdxlres(1536, 640)}", inputs=None, outputs=None, show_progress=False)
                                
                            button5.click(fn=None, _js="function(){setsdxlres(896, 1152)}", inputs=None, outputs=None, show_progress=False)
                            button6.click(fn=None, _js="function(){setsdxlres(832, 1216)}", inputs=None, outputs=None, show_progress=False)
                            button7.click(fn=None, _js="function(){setsdxlres(768, 1344)}", inputs=None, outputs=None, show_progress=False)
                            button8.click(fn=None, _js="function(){setsdxlres(640, 1536)}", inputs=None, outputs=None, show_progress=False)

            return []
