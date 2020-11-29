import pygame
import glm
import numpy as np

from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from obj import Obj

class Pumpkin(object):
    def __init__(self, fileName, textureName):
        self.model = Obj(fileName)

        self.create_vertex_buffer()

        self.texture_surface    =   pygame.image.load(textureName)
        self.texture_data       =   pygame.image.tostring(self.texture_surface, "RGB", 1)
        self.texture            =   glGenTextures(1)

        self.position   =   glm.vec3(0, 0, 0)
        self.rotation   =   glm.vec3(0, 270, 0)
        self.scale      =   glm.vec3(1, 1, 1)

    def get_matrix(self):
        i = glm.mat4(1)

        translate   =   glm.translate(i, self.position)
        
        pitch       =   glm.rotate(i, glm.radians(self.rotation.x), glm.vec3(1, 0, 0))
        yaw         =   glm.rotate(i, glm.radians(self.rotation.y), glm.vec3(0, 1, 0))
        roll        =   glm.rotate(i, glm.radians(self.rotation.z), glm.vec3(0, 0, 1))
        
        rotate      =   pitch * yaw * roll
        
        scale       =   glm.scale(i, self.scale)
        
        return translate * rotate * scale

    def create_vertex_buffer(self):
        buffer = []

        for face in self.model.faces:
            for i in range(3):
                #   VERTICES
                buffer.append(self.model.vertices[face[i][0] - 1][0])
                buffer.append(self.model.vertices[face[i][0] - 1][1])
                buffer.append(self.model.vertices[face[i][0] - 1][2])
                buffer.append(1)

                #   NORMALES
                buffer.append(self.model.normals[face[i][2] - 1][0])
                buffer.append(self.model.normals[face[i][2] - 1][1])
                buffer.append(self.model.normals[face[i][2] - 1][2])
                buffer.append(0)

                #   TEXTURA
                buffer.append(self.model.texcoords[face[i][1] - 1][0])
                buffer.append(self.model.texcoords[face[i][1] - 1][1])

        self.vertex_buffer = np.array( buffer, dtype=np.float32)


    def render_in_scene(self):

        VBO = glGenBuffers(1)
        VAO = glGenVertexArrays(1)
        
        glBindVertexArray(VAO)

        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, self.vertex_buffer.nbytes, self.vertex_buffer, GL_STATIC_DRAW)

        glVertexAttribPointer(0, 4, GL_FLOAT, GL_FALSE, 4 * 10, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glVertexAttribPointer(1, 4, GL_FLOAT, GL_FALSE, 4 * 10, ctypes.c_void_p(4 * 4))
        glEnableVertexAttribArray(1)

        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 4 * 10, ctypes.c_void_p(4 * 8))
        glEnableVertexAttribArray(2)

        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, self.texture_surface.get_width(), self.texture_surface.get_height(), 0, GL_RGB, GL_UNSIGNED_BYTE, self.texture_data)
        glGenerateMipmap(GL_TEXTURE_2D)

        glDrawArrays(GL_TRIANGLES, 0, len(self.model.faces) * 3)

class F1(object):
    def __init__(self, fileName, textureName):
        self.model = Obj(fileName)

        self.create_vertex_buffer()

        self.texture_surface    =   pygame.image.load(textureName)
        self.texture_data       =   pygame.image.tostring(self.texture_surface, "RGB", 1)
        self.texture            =   glGenTextures(1)

        self.position   =   glm.vec3(0, 0, 0)
        self.rotation   =   glm.vec3(0, 90, 0)
        self.scale      =   glm.vec3(0.1, 0.1, 0.1)

    def get_matrix(self):
        i = glm.mat4(1)

        translate   =   glm.translate(i, self.position)
        
        pitch       =   glm.rotate(i, glm.radians(self.rotation.x), glm.vec3(1, 0, 0))
        yaw         =   glm.rotate(i, glm.radians(self.rotation.y), glm.vec3(0, 1, 0))
        roll        =   glm.rotate(i, glm.radians(self.rotation.z), glm.vec3(0, 0, 1))
        
        rotate      =   pitch * yaw * roll
        
        scale       =   glm.scale(i, self.scale)
        
        return translate * rotate * scale

    def create_vertex_buffer(self):
        buffer = []

        for face in self.model.faces:
            for i in range(3):
                #   VERTICES
                buffer.append(self.model.vertices[face[i][0] - 1][0])
                buffer.append(self.model.vertices[face[i][0] - 1][1])
                buffer.append(self.model.vertices[face[i][0] - 1][2])
                buffer.append(1)

                #   NORMALES
                buffer.append(self.model.normals[face[i][2] - 1][0])
                buffer.append(self.model.normals[face[i][2] - 1][1])
                buffer.append(self.model.normals[face[i][2] - 1][2])
                buffer.append(0)

                #   TEXTURA
                buffer.append(self.model.texcoords[face[i][1] - 1][0])
                buffer.append(self.model.texcoords[face[i][1] - 1][1])

        self.vertex_buffer = np.array( buffer, dtype=np.float32)


    def render_in_scene(self):

        VBO = glGenBuffers(1)
        VAO = glGenVertexArrays(1)
        
        glBindVertexArray(VAO)

        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, self.vertex_buffer.nbytes, self.vertex_buffer, GL_STATIC_DRAW)

        glVertexAttribPointer(0, 4, GL_FLOAT, GL_FALSE, 4 * 10, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glVertexAttribPointer(1, 4, GL_FLOAT, GL_FALSE, 4 * 10, ctypes.c_void_p(4 * 4))
        glEnableVertexAttribArray(1)

        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 4 * 10, ctypes.c_void_p(4 * 8))
        glEnableVertexAttribArray(2)

        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, self.texture_surface.get_width(), self.texture_surface.get_height(), 0, GL_RGB, GL_UNSIGNED_BYTE, self.texture_data)
        glGenerateMipmap(GL_TEXTURE_2D)

        glDrawArrays(GL_TRIANGLES, 0, len(self.model.faces) * 3)

class Renault(object):
    def __init__(self, fileName, textureName):
        self.model = Obj(fileName)

        self.create_vertex_buffer()

        self.texture_surface    =   pygame.image.load(textureName)
        self.texture_data       =   pygame.image.tostring(self.texture_surface, "RGB", 1)
        self.texture            =   glGenTextures(1)

        self.position   =   glm.vec3(0, 0, 0)
        self.rotation   =   glm.vec3(0, 270, 0)
        self.scale      =   glm.vec3(0.1, 0.1, 0.1)

    def get_matrix(self):
        i = glm.mat4(1)

        translate   =   glm.translate(i, self.position)
        
        pitch       =   glm.rotate(i, glm.radians(self.rotation.x), glm.vec3(1, 0, 0))
        yaw         =   glm.rotate(i, glm.radians(self.rotation.y), glm.vec3(0, 1, 0))
        roll        =   glm.rotate(i, glm.radians(self.rotation.z), glm.vec3(0, 0, 1))
        
        rotate      =   pitch * yaw * roll
        
        scale       =   glm.scale(i, self.scale)
        
        return translate * rotate * scale

    def create_vertex_buffer(self):
        buffer = []

        for face in self.model.faces:
            for i in range(3):
                #   VERTICES
                buffer.append(self.model.vertices[face[i][0] - 1][0])
                buffer.append(self.model.vertices[face[i][0] - 1][1])
                buffer.append(self.model.vertices[face[i][0] - 1][2])
                buffer.append(1)

                #   NORMALES
                buffer.append(self.model.normals[face[i][2] - 1][0])
                buffer.append(self.model.normals[face[i][2] - 1][1])
                buffer.append(self.model.normals[face[i][2] - 1][2])
                buffer.append(0)

                #   TEXTURA
                buffer.append(self.model.texcoords[face[i][1] - 1][0])
                buffer.append(self.model.texcoords[face[i][1] - 1][1])

        self.vertex_buffer = np.array( buffer, dtype=np.float32)


    def render_in_scene(self):

        VBO = glGenBuffers(1)
        VAO = glGenVertexArrays(1)
        
        glBindVertexArray(VAO)

        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, self.vertex_buffer.nbytes, self.vertex_buffer, GL_STATIC_DRAW)

        glVertexAttribPointer(0, 4, GL_FLOAT, GL_FALSE, 4 * 10, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glVertexAttribPointer(1, 4, GL_FLOAT, GL_FALSE, 4 * 10, ctypes.c_void_p(4 * 4))
        glEnableVertexAttribArray(1)

        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 4 * 10, ctypes.c_void_p(4 * 8))
        glEnableVertexAttribArray(2)

        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, self.texture_surface.get_width(), self.texture_surface.get_height(), 0, GL_RGB, GL_UNSIGNED_BYTE, self.texture_data)
        glGenerateMipmap(GL_TEXTURE_2D)

        glDrawArrays(GL_TRIANGLES, 0, len(self.model.faces) * 3)

class Jet(object):
    def __init__(self, fileName, textureName):
        self.model = Obj(fileName)

        self.create_vertex_buffer()

        self.texture_surface    =   pygame.image.load(textureName)
        self.texture_data       =   pygame.image.tostring(self.texture_surface, "RGB", 1)
        self.texture            =   glGenTextures(1)

        self.position   =   glm.vec3(0, 0, 0)
        self.rotation   =   glm.vec3(0, 90, 0)
        self.scale      =   glm.vec3(1, 1, 1)

    def get_matrix(self):
        i = glm.mat4(1)

        translate   =   glm.translate(i, self.position)
        
        pitch       =   glm.rotate(i, glm.radians(self.rotation.x), glm.vec3(1, 0, 0))
        yaw         =   glm.rotate(i, glm.radians(self.rotation.y), glm.vec3(0, 1, 0))
        roll        =   glm.rotate(i, glm.radians(self.rotation.z), glm.vec3(0, 0, 1))
        
        rotate      =   pitch * yaw * roll
        
        scale       =   glm.scale(i, self.scale)
        
        return translate * rotate * scale

    def create_vertex_buffer(self):
        buffer = []

        for face in self.model.faces:
            for i in range(3):
                #   VERTICES
                buffer.append(self.model.vertices[face[i][0] - 1][0])
                buffer.append(self.model.vertices[face[i][0] - 1][1])
                buffer.append(self.model.vertices[face[i][0] - 1][2])
                buffer.append(1)

                #   NORMALES
                buffer.append(self.model.normals[face[i][2] - 1][0])
                buffer.append(self.model.normals[face[i][2] - 1][1])
                buffer.append(self.model.normals[face[i][2] - 1][2])
                buffer.append(0)

                #   TEXTURA
                buffer.append(self.model.texcoords[face[i][1] - 1][0])
                buffer.append(self.model.texcoords[face[i][1] - 1][1])

        self.vertex_buffer = np.array( buffer, dtype=np.float32)


    def render_in_scene(self):

        VBO = glGenBuffers(1)
        VAO = glGenVertexArrays(1)
        
        glBindVertexArray(VAO)

        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, self.vertex_buffer.nbytes, self.vertex_buffer, GL_STATIC_DRAW)

        glVertexAttribPointer(0, 4, GL_FLOAT, GL_FALSE, 4 * 10, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glVertexAttribPointer(1, 4, GL_FLOAT, GL_FALSE, 4 * 10, ctypes.c_void_p(4 * 4))
        glEnableVertexAttribArray(1)

        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 4 * 10, ctypes.c_void_p(4 * 8))
        glEnableVertexAttribArray(2)

        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, self.texture_surface.get_width(), self.texture_surface.get_height(), 0, GL_RGB, GL_UNSIGNED_BYTE, self.texture_data)
        glGenerateMipmap(GL_TEXTURE_2D)

        glDrawArrays(GL_TRIANGLES, 0, len(self.model.faces) * 3)



class Renderer(object):
    def __init__(self, screen):
        self.SCREEN = screen
        _, _, self.WIDTH, self.HEIGHT = screen.get_rect()

        glEnable(GL_DEPTH_TEST)
        glViewport(0, 0, self.WIDTH, self.HEIGHT)

        self.temp = 0

        self.model_lists = []

        self.camera_position    =   glm.vec3(0, 0, 0)
        self.camera_rotation    =   glm.vec3(0, 0, 0)

        # Light
        self.point_light        =   glm.vec4(0, 0, 0, 0)

        # Perspective Projection Matrix
        self.projection         =   glm.perspective(glm.radians(60), self.WIDTH / self.HEIGHT, 0.1, 1000)

    def get_view_matrix(self):
        i = glm.mat4(1)

        camera_translate    =   glm.translate(i, self.camera_position)
        
        camera_pitch        =   glm.rotate(i, glm.radians(self.camera_rotation.x), glm.vec3(1, 0, 0))
        camera_yaw          =   glm.rotate(i, glm.radians(self.camera_rotation.y), glm.vec3(0, 1, 0))
        camera_roll         =   glm.rotate(i, glm.radians(self.camera_rotation.z), glm.vec3(0, 0, 1))
        
        camera_rotate       =   camera_pitch * camera_yaw * camera_roll

        view = glm.lookAt(self.camera_position, glm.vec3(0, 0, 0), glm.vec3(0, 1, 0))
        
        return glm.inverse( camera_translate * camera_rotate )

    def wireframe_mode(self):
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    def filled_mode(self):
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)


    def set_shaders(self, vertex_shader, fragment_shader):

        if vertex_shader is not None or fragment_shader is not None:
            self.active_shader = compileProgram(
                compileShader(vertex_shader, GL_VERTEX_SHADER),
                compileShader(fragment_shader, GL_FRAGMENT_SHADER)
            )

        else:
            self.active_shader = None

        glUseProgram(self.active_shader)


    def render(self):

        glClearColor(0.2, 0.2, 0.2, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )


        if self.active_shader:
            glUniformMatrix4fv(
                glGetUniformLocation(self.active_shader, "view"),
                1, GL_FALSE, glm.value_ptr(self.get_view_matrix())
            )

            glUniformMatrix4fv(
                glGetUniformLocation(self.active_shader, "projection"),
                1, GL_FALSE, glm.value_ptr(self.projection)
            )

            glUniform4f(
                glGetUniformLocation(self.active_shader, "light"), 
                self.point_light.x, self.point_light.y, self.point_light.z, self.point_light.w
            )

            glUniform4f(
                glGetUniformLocation(self.active_shader, "color"), 
                1, 1, 1, 1
            )


        for model in self.model_lists:
            if self.active_shader:
                glUniformMatrix4fv(
                    glGetUniformLocation(self.active_shader, "model"),
                    1, GL_FALSE, glm.value_ptr(model.get_matrix())
                )

            model.render_in_scene()