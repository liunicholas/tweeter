import React, { useState } from "react";
import {
  View,
  Image,
  TextInput,
  StyleSheet,
  TouchableOpacity,
  Text,
} from "react-native";
import * as ImagePicker from "expo-image-picker";
import { Ionicons } from "@expo/vector-icons";

// Define props interface
interface PostInputProps {
  value: string;
  onChangeText: (text: string) => void;
  onSubmit: () => void;
  isPosting: boolean;
  previewImage: string | undefined;
  setPreviewImage: (image: string | undefined) => void;
}

// PostInput handles the creation of new posts
// It contains the input field and submit button
export const PostInput: React.FC<PostInputProps> = ({
  value,
  onChangeText,
  onSubmit,
  isPosting,
  previewImage,
  setPreviewImage,
}) => {
  const takePhoto = async () => {
    const { status } = await ImagePicker.requestCameraPermissionsAsync();
    if (status !== "granted") {
      alert("Camera permission not granted");
      return;
    }

    const result = await ImagePicker.launchCameraAsync({
      quality: 0.8,
      allowsEditing: true,
      aspect: [4, 3],
    });
    if (!result.canceled) {
      setPreviewImage(result.assets[0].uri);
    }
  };

  const pickImage = async () => {
    const { status } = await ImagePicker.requestMediaLibraryPermissionsAsync();
    if (status !== "granted") {
      alert("Gallery permission not granted");
      return;
    }

    const result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      quality: 0.8,
      allowsEditing: true,
      aspect: [4, 3],
    });
    if (!result.canceled) {
      setPreviewImage(result.assets[0].uri);
    }
  };

  return (
    <View style={styles.container}>
      {/* Input field for post content */}
      <TextInput
        style={styles.input}
        value={value}
        onChangeText={onChangeText}
        placeholder="Write your post..."
        // Disable input while posting
        editable={!isPosting}
        multiline
      />

      {/* Submit button with loading state */}
      <View style={styles.inputContainer}>
        <View style={styles.actionButtons}>
          <TouchableOpacity
            style={[
              styles.iconButton,
              isPosting || !value.trim() ? styles.iconButtonDisabled : null,
            ]}
            onPress={onSubmit}
            disabled={isPosting || !value.trim()}
          >
            <Ionicons
              name="send"
              size={24}
              color={isPosting || !value.trim() ? "#999" : "#007AFF"}
            />
          </TouchableOpacity>
          <View style={styles.imageButtons}>
            <TouchableOpacity style={styles.iconButton} onPress={takePhoto}>
              <Ionicons name="camera" size={24} color="#007AFF" />
            </TouchableOpacity>
            <TouchableOpacity style={styles.iconButton} onPress={pickImage}>
              <Ionicons name="images" size={24} color="#007AFF" />
            </TouchableOpacity>
          </View>
        </View>
      </View>
      {previewImage && (
        <View style={styles.imageWrapper}>
          <Image source={{ uri: previewImage }} style={styles.image} />
          <TouchableOpacity
            style={styles.deleteButton}
            onPress={() => setPreviewImage(undefined)}
          >
            <Ionicons
              name="close-circle"
              size={24}
              color="rgba(255, 255, 255, 0.9)"
            />
          </TouchableOpacity>
        </View>
      )}
    </View>
  );
};

// Styles for the PostInput component
const styles = StyleSheet.create({
  container: {
    marginBottom: 20,
    backgroundColor: "#ffffff",
    borderRadius: 8,
    padding: 16,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  input: {
    borderWidth: 1,
    borderColor: "#e0e0e0",
    borderRadius: 4,
    padding: 12,
    marginBottom: 12,
    minHeight: 100,
    textAlignVertical: "top",
  },
  inputContainer: {
    marginBottom: 12,
  },
  actionButtons: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
  },
  imageButtons: {
    flexDirection: "row",
    gap: 8,
  },
  iconButton: {
    padding: 8,
    borderRadius: 20,
    backgroundColor: "#f0f0f0",
  },
  iconButtonDisabled: {
    opacity: 0.5,
  },
  imageWrapper: {
    position: "relative",
    marginTop: 4,
  },
  image: {
    width: "100%",
    height: 200,
    borderRadius: 8,
    marginBottom: 12,
  },
  deleteButton: {
    position: "absolute",
    top: 8,
    right: 8,
    width: 24,
    height: 24,
    justifyContent: "center",
    alignItems: "center",
  },
});
