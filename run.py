import os


image_path = r'/data1/zjw/Dataset/ancient_character/test_images/401206800-J0001-3-000448-001-00002.jpg'

box_thresh = 0.0005
thresh = 0.01
image_short_side = 736

# totaltest
resume = r'/data1/zjw/checkpoint/DB/synthtext_totaltext_res50_dcn_fpn_scale_spatial'
exp = r'/data1/zjw/researchData/DB-OCR/experiments/seg_detector/totaltext_resnet50_deform_thre.yaml'

# resume = r'/data1/zjw/checkpoint/DB/totaltext_resnet50'
# exp = r'/data1/zjw/researchData/DB-OCR/experiments/seg_detector/base_totaltext.yaml'


# resume = r'/data1/zjw/checkpoint/DB/synthtext_td500_res50_dcn_fpn_scale_spatial'
# exp = r'/data1/zjw/researchData/DB-OCR/experiments/seg_detector/td500_resnet50_deform_thre.yaml'

os.system(
        f'CUDA_VISIBLE_DEVICES=0  \
        python demo.py  {exp} \
            --image_path {image_path} \
            --resume {resume}  \
            --box_thresh {box_thresh} \
            --visualize \
            --image_short_side {image_short_side}\
            --thresh {thresh}')

